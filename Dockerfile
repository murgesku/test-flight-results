FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

RUN pip install --upgrade pip
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir --requirement /tmp/requirements.txt