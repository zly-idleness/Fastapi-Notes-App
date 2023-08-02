FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# for migration
# to run migration, use `docker-compose exec backend aerich migrate`
# to run upgrade,  use `docker-compose exec backend aerich upgrade`
COPY migrations/ .
COPY pyproject.toml .

COPY src/ .
