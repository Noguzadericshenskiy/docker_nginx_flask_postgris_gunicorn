FROM python:3.8-alpine

WORKDIR /backend

COPY requirements.txt /backend
RUN pip install --upgrade pip -r requirements.txt

COPY . /backend

EXPOSE 5000