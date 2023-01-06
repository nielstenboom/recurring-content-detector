FROM python:3.9

WORKDIR /opt

COPY ./recurring_content_detector /opt/recurring-content-detector/recurring_content_detector
COPY setup.py /opt/recurring-content-detector/setup.py 

WORKDIR /opt/recurring-content-detector

RUN pip install . && \
    apt-get update --allow-releaseinfo-change && \
    apt-get install libglib2.0-0 -y && \
    apt-get install -y libsm6 libxext6 libxrender-dev -y && \
    apt-get install ffmpeg -y
