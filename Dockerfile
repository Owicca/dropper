FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app/ /app/

WORKDIR /app/

RUN pip install poetry
