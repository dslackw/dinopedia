FROM python:3.9.12

RUN apt-get update && apt-get install -y libpq5

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app

WORKDIR /app

COPY . /app
