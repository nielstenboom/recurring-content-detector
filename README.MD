# Recurring content detector / credits detector

This repository contains the code that was used to conduct experiments for a master's thesis LINK TODO. The goal was to detect recaps, opening credits, closing credits and previews from video files in an unsupervised manner.

The experiments done in the master's thesis were done in the jupyter notebooks, but as the code in these got quite messy. I packed the used code in a python package so that it can be used more easily.

MAKE SURE THE VIDEO FILES YOU USE THIS ARE IN THE RIGHT ALPHABETICAL ORDER BASED ON WHEN THEY PLAY IN THE SEASON. You'll get weird results if it does not. So episode 1 above episode 2 etc.

# Installation

Clone the code somewhere you prefer. Then do the following steps (assuming you have an anaconda setup) if you want to run the program with the default settings:

```
cd recurring_content_detector
wget -P recurring_content_detector/keras_rmac/data https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_th_dim_ordering_th_kernels.h5
conda install faiss-cpu -c pytorch
pip install mkl
pip install .
```

Make sure [ffmpeg](https://ffmpeg.org/) is in the PATH variable.

Then you can run the detector in a python program in the following way:

```
import recurring_content_detector as rcd
rcd.detect("/directory/with/season/videofiles")
```

#### Instructions to run with different parameters

If for some reason you want the program to run with different parameters or changed code, you can take the following steps:

- Clone the code somewhere you like.
- Copy the directory recurring-content-detector/recurring_content_detector to your project.
- Change code / parameters (residing in config.py)
- from within the directory run `pip install -r requirements.txt`
- Install faiss and mkl as described above
- the detector is now ready to be used within your project

```
import recurring_content_detector as rcd
rcd.detect("/directory/with/season/videofiles")
```

## Recurring content detection

With this code it is possible to detect recaps, opening credits, closing credits and previews up to a certain extent. The following image gives a schematic overview of how it works: 

<p align="center">
<img src="images/thesisdiagram.png?raw=true">
</p>

## Annotations

If you want to quantitively test out how well this works on your own data, fill in the [annotations](annotations_example.csv) file and supply it as the second parameter.
```
rcd.detect("/directory/with/season/videofiles", annotations = "path/to/annotations.csv")
```
 When the program is done, it will output precision and recall scores based on the supplied annotations.