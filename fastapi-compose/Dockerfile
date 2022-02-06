FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

RUN apt-get update

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app