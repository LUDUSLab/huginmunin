FROM python:3

WORKDIR /app

COPY docker/flask/uwsgi.ini .
COPY app.py .
COPY requirements.txt .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]