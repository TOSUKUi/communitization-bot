FROM python:3.9.16-slim-buster

RUN pip3 install --upgrade pip \
    && pip3 install poetry

WORKDIR /app

COPY ./ ./
RUN poetry install --only main

CMD ["poetry", "run", "python", "main.py"]
