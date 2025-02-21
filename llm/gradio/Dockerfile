FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir gradio requests

EXPOSE 7860

ENV GRADIO_SERVER_NAME=0.0.0.0

CMD ["python", "app.py"]

