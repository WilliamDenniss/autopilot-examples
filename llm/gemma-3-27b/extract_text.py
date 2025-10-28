import json
import sys

def extract_text(json_string):
    """
    Parses a JSON string from the vLLM server and extracts the generated text.

    Args:
        json_string: The JSON string to parse.

    Returns:
        The extracted text as a string.
    """
    try:
        data = json.loads(json_string)
        return data["choices"][0]["text"]
    except (json.JSONDecodeError, IndexError, KeyError) as e:
        return f"Error parsing JSON: {e}"

if __name__ == "__main__":
    # Check if there is input from stdin
    if not sys.stdin.isatty():
        json_input = sys.stdin.read()
        extracted_text = extract_text(json_input)
        print(extracted_text)
    else:
        print("Usage: curl ... | python extract_text.py")
