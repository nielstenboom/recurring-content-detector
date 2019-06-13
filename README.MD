# Recurring content detector / credits detector

This repository contains the code that was used to conduct experiments for a master's thesis LINK TODO. The goal was to detect recaps, opening credits, closing credits and previews from video files in an unsupervised manner.

The experiments done in the master's thesis were done in the jupyter notebooks, but as the code in these got quite messy. I packed the used code in a python package so that it can be used more easily.

This project uses / credits to:
- https://github.com/noagarcia/keras_rmac for the CNN vectors 
- https://github.com/facebookresearch/faiss for the efficient matching of the feature vectors 

## Installation

To install the package, do the following steps (assuming you have an anaconda setup with python 3.6) if you want to run the program with the default settings:

```
git clone https://github.com/nielstenboom/recurring-content-detector.git
cd recurring-content-detector
wget -P recurring_content_detector/keras_rmac/data https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_th_dim_ordering_th_kernels.h5
conda install faiss-cpu -c pytorch
pip install mkl
(optional: change parameters in recurring_content_detector/config.py)
pip install .
```

It is also possible to build a docker container that does these steps for you with the [Dockerfile](Dockerfile) in the directory.

Make sure [ffmpeg](https://ffmpeg.org/) is in the PATH variable and that [tensorflow](https://www.tensorflow.org/install/pip) is installed.

Run `pip uninstall recurring-content-detector` to uninstall the package.

## Recurring content detection

With this code it is possible to detect recaps, opening credits, closing credits and previews in video files from a TV-show unsupervised up to a certain extent. The following image gives a schematic overview of how it works: 

<p align="center">
<img src="images/thesisdiagram.png?raw=true">
</p>

If the installation was succesful then you can run the detector in a python program in the following way:

```
import recurring_content_detector as rcd
rcd.detect("/directory/with/season/videofiles")
```

Make sure the video files you used can be sorted in the right alphabetical order similar as to when they play in the season! So episode_1 -> episode_2 -> episode_3 -> etc.. You'll get weird results otherwise.

It will take some time as video processing takes quite some resources. An application in production should run it in parallel.


## Annotations

If you want to quantitively test out how well this works on your own data, fill in the [annotations](annotations_example.csv) file and supply it as the second parameter.
```
rcd.detect("/directory/with/season/videofiles", annotations = "path/to/annotations.csv")
```
 When the program is done, it will output precision and recall scores based on the supplied annotations.