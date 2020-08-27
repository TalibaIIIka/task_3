FROM python:3.7.9-slim

WORKDIR /usr/src/app

COPY ./app/ /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt

CMD ["python", "-m", "web_app"]