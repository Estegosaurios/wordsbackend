FROM python:3.7-alpine
RUN apk add --update --no-cache \
    python3 \
    python3-dev \
    gcc \
    musl-dev \
    libffi-dev \
    libressl-dev \
    postgresql-dev

WORKDIR /opt/wordsbackend

COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh
COPY manage.py manage.py
COPY wordsbackend wordsbackend

RUN pip install -r requirements.txt

