import os

import openai
from llama_index.llms import OpenAI
from werkzeug.utils import secure_filename
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from llama_index import VectorStoreIndex, Document, SimpleDirectoryReader, ServiceContext, set_global_service_context
from dotenv import load_dotenv

import os  # Load environment variables

load_dotenv()

# Initialize OpenAI API with your key
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=2048)
# %%
service_context = ServiceContext.from_defaults(llm=llm)
set_global_service_context(service_context=service_context)


class DocumentProcessor:
    ALLOWED_EXTENSIONS = {'txt', 'pdf'}
    UPLOAD_FOLDER = 'uploads'

    def __init__(self):
        load_dotenv()
        sensitive_docs = SimpleDirectoryReader(input_files=["SensitiveToy.pdf"]).load_data()
        self.sensitive_index = VectorStoreIndex.from_documents(sensitive_docs)
        self.sensitive_engine = self.sensitive_index.as_query_engine(similarity_top_k=3)
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def safe_search(self, text):
        results = self.analyzer.analyze(text=text, language='en')
        return self.anonymizer.anonymize(text=text, analyzer_results=results)

    def upload_file(self, file_content, filename):
        if filename == '':
            raise ValueError('No selected file')
        if self.allowed_file(filename):
            filename = secure_filename(filename)
            filepath = os.path.join(self.UPLOAD_FOLDER, filename)
            with open(filepath, 'wb') as f:
                f.write(file_content.read())

            # Process and add to index
            with open(filepath, 'r') as f:
                content = f.read()
                doc = Document(content, doc_id=filename)
                self.sensitive_index.insert(doc)

            return filename
        else:
            raise ValueError('File not allowed')

    def query_unsafe(self, query):
        if not query:
            raise ValueError("Query parameter is required.")
        response = self.sensitive_engine.query(query)
        return response

    def query_safe(self, query):
        if not query:
            raise ValueError("Query parameter is required.")
        response = self.sensitive_engine.query(query)
        safe_response = self.safe_search(str(response))
        return safe_response
