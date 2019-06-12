# Recurring content detector / credits detector

This repository contains the code that was used to conduct experiments for a master's thesis LINK TODO. The goal was to detect recaps, opening credits, closing credits and previews from video files in an unsupervised manner.

The experiments done in the master's thesis were done in the jupyter notebooks, but as the code in these got quite messy. I packed the used code in a python package so that it can be used more easily.

This project uses / credits to:
- https://github.com/noagarcia/keras_rmac for the CNN vectors 
- https://github.com/facebookresearch/faiss for the efficient matching of the feature vectors 

# Installation

Clone the code somewhere you prefer. Then do the following steps (assuming you have an anaconda setup) if you want to run the program with the default settings:

```
cd recurring-content-detector
wget -P recurring_content_detector/keras_rmac/data https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_th_dim_ordering_th_kernels.h5
conda install faiss-cpu -c pytorch
pip install mkl
pip install .
```

Make sure [ffmpeg](https://ffmpeg.org/) is in the PATH variable and that tensorflow is installed.


#### Instructions to run with different parameters

If for some reason you want the program to run with different parameters or changed code, you can take the following steps:

- Clone the code somewhere you like.
- Copy the directory recurring-content-detector/recurring_content_detector to your project.
- Change code / parameters (residing in config.py)
- from within the directory run `pip install -r requirements.txt`
- Install faiss and mkl as described above
- the detector is now ready to be used within your project


## Recurring content detection

With this code it is possible to detect recaps, opening credits, closing credits and previews up to a certain extent. The following image gives a schematic overview of how it works: 

<p align="center">
<img src="images/thesisdiagram.png?raw=true">
</p>

If the installation was succesful then you can run the detector in a python program in the following way:

```
import recurring_content_detector as rcd
rcd.detect("/directory/with/season/videofiles")
```

Make sure the video files you used are in the right alphabetical order similar as to when they play in the season! So episode_1 -> episode_2 -> episode_3 -> etc.. You'll get weird results otherwise.

It will take some time as video processing takes quite some resources. An application in production should run it in parallel.


## Annotations

If you want to quantitively test out how well this works on your own data, fill in the [annotations](annotations_example.csv) file and supply it as the second parameter.
```
rcd.detect("/directory/with/season/videofiles", annotations = "path/to/annotations.csv")
```
 When the program is done, it will output precision and recall scores based on the supplied annotations.