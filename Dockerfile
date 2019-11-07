FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

WORKDIR = /app

COPY . /app

ENV STATIC_URL /static
ENV STATIC_PATH /app/static
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
