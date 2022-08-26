FROM python:3.9.10-slim-buster

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install mysqlclient nba-api SQLAlchemy mysql-connector-python numpy

COPY ./src /app/src
COPY ./main.py /app/main.py
WORKDIR /app
CMD ["python", "main.py", "initialize"]
