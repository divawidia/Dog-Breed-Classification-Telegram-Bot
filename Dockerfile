# Use the official lightweight Python image.
# https://hub.docker.com/_/python
# FROM python:3.10-slim
FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install production dependencies.
RUN pip install -r requirements.txt

COPY . /app

CMD exec python3 tele_bot.py