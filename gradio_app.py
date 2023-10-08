import os

import openai
import gradio as gr
from dotenv import load_dotenv

from app import DocumentProcessor
load_dotenv()

# Initialize OpenAI API with your key
openai.api_key = os.getenv("OPENAI_API_KEY")

dp = DocumentProcessor()


def predict(message, history, mode, pdf_file):
    if mode == 'Safe':
        query_result = dp.query_safe(message)
    else:
        query_result = dp.query_unsafe(message)

    history_openai_format = [
        {"role": "system", "content": "You are helpful knowledge base. Always answer to your best ability. Only if there is a placeholder like <NAME> in the query, provide generic information without details."}]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message + "query result:" + str(query_result)})

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message


# Radio button for mode selection
mode_radio = gr.Radio(label="Mode", choices=["Safe", "Unsafe"], default="Safe")

# File input for PDF reading
pdf_input = gr.File(label="Upload PDF")

gr.ChatInterface(
    predict,
    additional_inputs=[
        mode_radio,
        pdf_input],
    chatbot=gr.Chatbot(height=500),
    description="OpenAI Gradio",
    title="OAI Gradio",
    theme=gr.themes.Default(primary_hue="green", secondary_hue="green")    ,
).queue().launch(share=True)
