FROM python:3.9.10-slim-buster

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install mysqlclient nba-api

COPY ./initialize.py /app/initialize.py
WORKDIR /app
CMD python ./initialize.py
