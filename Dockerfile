FROM conda/miniconda3

RUN conda install faiss-cpu -c pytorch
RUN pip install mkl


WORKDIR /opt

COPY . /opt/recurring-content-detector

WORKDIR /opt/recurring-content-detector

RUN pip install .

RUN apt-get update
RUN apt-get install libglib2.0-0 -y
RUN apt-get install -y libsm6 libxext6 libxrender-dev -y
RUN pip install opencv-python

RUN apt-get install ffmpeg -y
RUN pip install tensorflow
RUN conda update numpy -y
