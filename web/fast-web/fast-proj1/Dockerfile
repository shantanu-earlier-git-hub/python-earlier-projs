
from python:3.14.2

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app.bak/requirements.txt

COPY app.bak /app

CMD["fastapi","run","app/main.py","--port","80"]