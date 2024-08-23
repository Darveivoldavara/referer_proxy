FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt

COPY app.py /app/