FROM continuumio/miniconda3:4.7.12

WORKDIR /opt

COPY ./recurring_content_detector /opt/recurring-content-detector/recurring_content_detector
COPY setup.py /opt/recurring-content-detector/setup.py 

WORKDIR /opt/recurring-content-detector

RUN conda install python=3.6 -y && \
    pip install . && \
    apt-get update --allow-releaseinfo-change && \
    apt-get install libglib2.0-0 -y && \
    apt-get install -y libsm6 libxext6 libxrender-dev -y && \
    apt-get install ffmpeg -y && \
    conda install faiss-cpu=1.6.3 -c pytorch

    
