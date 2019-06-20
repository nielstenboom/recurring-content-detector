FROM conda/miniconda3

RUN conda install faiss-cpu -c pytorch
RUN pip install mkl


WORKDIR /opt

COPY . /opt/recurring-content-detector

WORKDIR /opt/recurring-content-detector

RUN apt-get update && apt-get install wget -y
RUN wget -P recurring_content_detector/keras_rmac/data https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_th_dim_ordering_th_kernels.h5
RUN pip install .

RUN apt-get update
RUN apt-get install libglib2.0-0 -y
RUN apt-get install -y libsm6 libxext6 libxrender-dev -y
RUN pip install opencv-python

RUN apt-get install ffmpeg -y
RUN pip install tensorflow
