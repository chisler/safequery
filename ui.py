# import gradio as gr
# import requests
#
# def handle_request(file, unsafe_query, safe_query):
#     if file is not None:
#         files = {'file': (file.name, file)}
#         response = requests.post("http://127.0.0.1:5000/upload", files=files)
#         return response.text, None, None
#     elif unsafe_query:
#         response = requests.get(f"http://127.0.0.1:5000/query_unsafe?query={unsafe_query}")
#         return None, response.text, None
#     elif safe_query:
#         response = requests.get(f"http://127.0.0.1:5000/query_safe?query={safe_query}")
#         return None, None, response.text
#     else:
#         return "Please provide input", None, None
#
# # Gradio UI
# iface = gr.Interface(
#     fn=handle_request,
#     inputs=[
#         gr.inputs.File(label="Upload File"),
#         gr.inputs.Textbox(label="Unsafe Query"),
#         gr.inputs.Textbox(label="Safe Query")
#     ],
#     outputs=[
#         "text",
#         "text",
#         "text"
#     ],
#     live=False
# )
#
# if __name__ == "__main__":
#     iface.launch()

import gradio as gr
import requests


def handle_request(file, unsafe_query, safe_query):
    if file is not None:
        files = {'file': (file.name, file)}
        response = requests.post("http://127.0.0.1:5000/upload", files=files)
        return response.text, None, None
    elif unsafe_query:
        response = requests.get(f"http://127.0.0.1:5000/query_unsafe?query={unsafe_query}")
        return None, response.text, None
    elif safe_query:
        response = requests.get(f"http://127.0.0.1:5000/query_safe?query={safe_query}")
        return None, None, response.text
    else:
        return "Please provide input", None, None


# Gradio UI
iface = gr.Interface(
    fn=handle_request,
    inputs=[
        gr.inputs.File(label="Upload File"),
        gr.inputs.Textbox(label="Unsafe Query"),
        gr.inputs.Textbox(label="Safe Query")
    ],
    outputs=[
        "text",
        "text",
        "text"
    ],
    live=False
)

if __name__ == "__main__":
    iface.launch()
