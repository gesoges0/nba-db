FROM python:3.9.10-slim-buster

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install mysqlclient==2.1.1 nba-api==1.1.11 SQLAlchemy==1.4.40 mysql-connector-python==8.0.30 numpy==1.23.2

COPY ./src /app/src
COPY ./main.py /app/main.py
WORKDIR /app
CMD ["python", "main.py", "initialize"]
