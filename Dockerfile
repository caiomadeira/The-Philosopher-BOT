FROM python:3.9

WORKDIR /PHILOBOT

COPY . .

RUN pip install -r requirements.txt
