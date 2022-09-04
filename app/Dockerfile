FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD flask_app.py /var/server/app.py
COPY . /app
WORKDIR /app
RUN chmod 777 /app
