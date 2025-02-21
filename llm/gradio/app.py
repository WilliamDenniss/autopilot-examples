import os
import gradio as gr
import requests

def query_vllm(input_text):
    model = os.getenv('MODEL_ID', 'unset-model-id')
    max_tokens = int(os.getenv('MAX_TOKENS', '9999'))
    temperature = float(os.getenv('TEMPERATURE', '0.6'))
    top_p = float(os.getenv('TOP_P', '0.95'))
    
    response = requests.post(
        "http://vllm-service:8000/v1/completions",
        json={
            "model": model,
            "prompt": input_text,
            "temperature": temperature,
            "top_p": top_p,            
            "max_tokens": max_tokens
        }
    )
    return response.json()["choices"][0]["text"]

iface = gr.Interface(fn=query_vllm, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860)
