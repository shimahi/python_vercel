FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev

COPY . .

WORKDIR /app/api

CMD uvicorn index:app --host 0.0.0.0 --port ${PORT}
