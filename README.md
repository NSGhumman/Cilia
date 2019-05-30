# Cilia Segmentation

## Introduction
Cilia are microscopic hair like structure that protrude form cell bodies. This project aims to implement methods to segment cilia pixels from a cell body video (grayscale time-series data). Presently, this project implements just one method - a statistical approach to distinguish cilia pixels from the static background. The full problem definition and the dataset can be found [here](https://github.com/dsp-uga/sp19/blob/master/projects/p2/project2.pdf).

<p align="center">
 <img align="center" src="https://i.ibb.co/SyT5ZVH/screen.png">
</p>


## Software Requirements
The following python libraries are required
 1. pillow
 2. numpy
 3. matplotlib

## The model
The model is a simple statistical one that anlyzes the grayscale variance of a pixel for classification.  To know about the method, refer the project Wiki.

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


