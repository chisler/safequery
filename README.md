# Document Processor Project

## Overview

The Document Processor project is a Python application designed to manage, analyze, and anonymize sensitive documents. It utilizes various libraries such as OpenAI, Llama Index, Werkzeug, and Presidio to handle document processing, indexing, and anonymization of sensitive information.

## Features

- **Document Upload**: Accepts text and PDF files, ensuring they are securely saved and processed.
- **Sensitive Data Anonymization**: Utilizes the Presidio Analyzer and Anonymizer engines to detect and anonymize sensitive information in the text.
- **Document Indexing**: Uses Llama Index to create a searchable index of documents.
- **Safe and Unsafe Query**: Allows querying the indexed documents and retrieving either raw or anonymized results.

## Prerequisites

- Python 3.8+
- Virtual Environment (recommended)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone [repository_url]
   cd [repository_directory]
   ```
2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables:**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
   Ensure that your API key is kept confidential and is not exposed to the public.

## Usage

### DocumentProcessor Class

The `DocumentProcessor` class is the core of the application, providing functionalities such as file upload, document indexing, and querying.

#### Methods

- `allowed_file(filename: str) -> bool`: Checks if the file has an allowed extension.
- `safe_search(text: str) -> str`: Analyzes and anonymizes sensitive information in the text.
- `upload_file(file_content, filename: str) -> str`: Uploads, saves, and indexes a document.
- `query_unsafe(query: str) -> Any`: Queries the index and retrieves raw results.
- `query_safe(query: str) -> str`: Queries the index and retrieves anonymized results.

### Example Usage

```python
doc_processor = DocumentProcessor()

# Upload a file
with open("example.txt", "rb") as file_content:
    filename = doc_processor.upload_file(file_content, "example.txt")

# Query the index
query = "search_term"
unsafe_results = doc_processor.query_unsafe(query)
safe_results = doc_processor.query_safe(query)
```

## Contributing

Contributions to the Document Processor project are welcome! Please ensure that you adhere to our coding standards and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- OpenAI for providing the GPT API.
- Microsoft Presidio for the anonymization engine.
- Llama Index for the document indexing capabilities.

---

**Note**: Ensure to adapt the README according to your project's specific details, repository structure, and additional features.