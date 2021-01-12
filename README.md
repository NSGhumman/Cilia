# Cilia Segmentation

## Introduction
Cilia are microscopic hair like structures protruding form cell walls of every cell in a human body. They beat in regular, rythmic patterns to perform a range of tasks from moving nutrients in to moving irritants out to amplifying cell-cell signaling pathways to generating calcium fluid flow in early cell differentiation. This project implements a method to detect and segment cilia pixels in a set of cell body videos (grayscale time-series data) obtained through nasal biopsies of human subjects. The work was done as part of the [Data Science Practicum](https://dsp-uga.github.io/sp19/) at University of Georgia - Athens, GA.

## Methods
Figure 2.1 shows the input and the expected output for the task. On the LEFT is a frame from one of the videos and on the RIGHT is the corresponding ground-truth label for the video. The cilia, as mentioned in the previous section, show movement while rest of the elements (background & cell) stay very stationary in comparison. The implemented method exploits this difference by computing variance in pixel intensities over time for all pixels and applying a segmentation threshold to separate out cilia pixels.

<p align="center">
 <img align="center" src="https://postimg.cc/1nNkyd1Z">
</p>

In the following pair of images, the LEFT one shows the results of computing pixel wise intensities as a heat map. The image on the right shows the output mask after thresholding.

<p align="center">
 <img align="center" src="https://i.ibb.co/SyT5ZVH/screen.png">
</p>


## Software Requirements
The implementation has the following Python dependencies:
 1. pillow
 2. numpy
 3. matplotlib

# How to run
Enter the source directory
```
cd src
```
and run the FStat module as
```
python FStat.py
```
The masks will be saved to the `predictions/` directory.

[Problem source](https://github.com/dsp-uga/sp19/blob/master/projects/p2/project2.pdf).
