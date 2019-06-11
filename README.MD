# Recurring content detector / credits detector

This repository contains the code that was used to conduct experiments for a master's thesis LINK.

The experiments done in the master's thesis were done in the jupyter notebooks, but as the code in these got quite messy. I packed the used code in a python package so that it can be used more easily.

# Installation

Clone the code somewhere you prefer. Then do the following steps (assuming you have an anaconda setup):

```
cd recurring_content_detector
pip install .
conda install faiss-cpu -c pytorch
```

And make sure [ffmpeg](https://ffmpeg.org/) is in the PATH variable.



## Recurring content detection

With this code it is possible to detect recaps, opening credits, closing credits and previews up to a certain extent. The following image gives a schematic overview of how it works: 

<p align="center">
<img src="images/thesisdiagram.png?raw=true">
</p>
