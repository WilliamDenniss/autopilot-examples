import os
import requests
import json
import gradio as gr

def stream_vllm(prompt):
    """A generator function that streams from vLLM and yields partial outputs.

    Whenever '</think>' is encountered in the text, we replace it with '<hr>'.
    """
    model = os.getenv('MODEL_ID', 'default-model-id')
    max_tokens = int(os.getenv('MAX_TOKENS', '9999'))
    temperature = float(os.getenv('TEMPERATURE', '0.6'))
    top_p = float(os.getenv('TOP_P', '0.95'))

    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "stream": True  # Enable streaming from vLLM
    }

    response = requests.post(
        "http://vllm-service:8000/v1/completions",
        json=payload,
        stream=True
    )

    accumulated_text = ""
    for line in response.iter_lines(decode_unicode=True):
        # Skip empty lines or lines not starting with 'data: '
        if not line or not line.startswith("data: "):
            continue

        data_str = line[len("data: "):]  # remove 'data: '
        if data_str.strip() == "[DONE]":
            break

        data = json.loads(data_str)
        chunk = data["choices"][0]["text"]

        accumulated_text += chunk
        # Replace '</think>' with <hr> in the output
        accumulated_text = accumulated_text.replace("</think>", "&lt;/think&gt;<hr>")

        yield accumulated_text  # Yield the entire generation so far

def main():
    with gr.Blocks() as demo:
        model = os.getenv('MODEL_ID', 'no-model-selected')
        gr.Markdown(f"# vLLM: {model}")
        
        input_box = gr.Textbox(label="Input", placeholder="Enter your prompt here")
        output_box = gr.Markdown(label="Generated Output (Markdown)")
        submit_button = gr.Button("Submit")

        # Pressing Enter inside the textbox triggers the same streaming function:
        input_box.submit(
            fn=stream_vllm,
            inputs=input_box,
            outputs=output_box,
            queue=True   # Recommended for streaming
        )

        # Clicking the button also triggers the streaming function:
        submit_button.click(
            fn=stream_vllm,
            inputs=input_box,
            outputs=output_box,
            queue=True   # Recommended for streaming
        )

    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
