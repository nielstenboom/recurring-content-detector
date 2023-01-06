FROM python:3.9-slim

WORKDIR /opt

COPY ./recurring_content_detector /opt/recurring-content-detector/recurring_content_detector
COPY setup.py /opt/recurring-content-detector/setup.py 

WORKDIR /opt/recurring-content-detector

RUN pip install . && \
    apt-get update && \
    apt-get install ffmpeg -y
