# Computational Design and Fabrication (CDF)

## Welcome

Welcome to **Computational Design and Fabrication**, a platform dedicated to beginner-friendly creative coding tutorials and exercises for computational design and fabrication in architecture.


## Session Blocks 
## General Computational Geometry

Title | Description | Slides | Session material | Assignment 
----- | ----------- | ------ | ---------------- | ----------
**01 Python Basics** | Quick start on Python | [Python Basics](https://docs.google.com/presentation/d/1fIpX7-DEaRLJhKe3QST4xTEx9U57yM9mbpVtvykUyD8/edit?usp=sharing) | https://github.com/robotic-fabrication-in-arch-classroom/session-01 | https://github.com/robotic-fabrication-in-arch-classroom/assignment-01
**02 Basic Geometry** | 2D and 3D primitive geometry  | [Geometry](https://docs.google.com/presentation/d/16DmLj11qJGcRS9t2plSShqpEKF18fyEFxWbCWRyrwEE/edit?usp=sharing) | https://github.com/robotic-fabrication-in-arch-classroom/session-02 | https://github.com/robotic-fabrication-in-arch-classroom/assignment-02
**03 Geometric Representations** | Mesh and Graph data structures and processing  | [Data Structures](https://docs.google.com/presentation/d/1lRxruAAzjBgQr4ochBbuwnfC7lbJ6FwgH7dUbuNIuC0/edit?usp=sharing) | https://github.com/robotic-fabrication-in-arch-classroom/session-04 | https://github.com/robotic-fabrication-in-arch-classroom/assignment-03
**04 Geometry Processing** | Transformation and morphing of mesh and graph geometries  | [Frames and Transformations](https://docs.google.com/presentation/d/1kMZ3cG7GBg3h3EDVvI_GPqTRwIeRn_IKUbUgkiBQ6sg/edit?usp=sharing) | https://github.com/robotic-fabrication-in-arch-classroom/session-03 | https://github.com/robotic-fabrication-in-arch-classroom/assignment-04

## Session Blocks 
## Associated With the Design Tool

Title | Description | Slides | Session material | Assignment 
----- | ----------- | ------ | ---------------- | ----------
**05 Earth 3D Printing Demo** | Earth 3D Printing Demo | [Earth 3D Printing Demo](LINK) | No assignment
**06 Surface Form Finding** | Geometric form finding for compression-only structures | [Form Finding](LINK) | https://github.com/robotic-fabrication-in-arch-classroom/session-05
**07 Volume Form Finding** | Geometric form finding for compression-only structures | [Form Finding](LINK) | https://github.com/robotic-fabrication-in-arch-classroom/session-05
**08 Shape Segmentation** | Segmentation and connection detailing | [Form Finding](LINK) | https://github.com/robotic-fabrication-in-arch-classroom/session-05
**09 Slicing and Print Path Generation** | Slicing and Print Path generation | [Slicing and Print Path Generation](LINK) | https://github.com/robotic-fabrication-in-arch-classroom/session-06


## Requirements

* Windows 10 Professional
* Rhino 7 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

## Dependencies

* [COMPAS](https://compas-dev.github.io/)

* [matplotlib](https://matplotlib.org/)
* [COMPAS Viewer](https://compas.dev/compas_viewer/latest/index.html)


## Getting started

### Setting up the Anaconda environment

Execute the commands below in Anaconda Prompt:
	
#### Installation

    (base) conda config --add channels conda-forge
    (base) conda create -n cdf compas
    (base) conda activate cdf
    
#### Verify Installation

    (cdf) pip show compas

####
    Name: COMPAS
    Version: 2.0.2
    Summary: The COMPAS framework
    ...

#### Installation of dependencies
    conda install matplotlib
    pip install compas_viewer
    
#### Installation for Rhino

    (cdf) python -m compas_rhino.install -v 7.0


### Cloning the CDF Repository

* Firstly, create a **workspace** directory in your File Explorer:

    C:\Users\your_username\workspace

* Secondly, open Github Desktop and clone the [CDF repository](https://github.com/computational_design_and_fabrication/computational_design_and_fabrication) into your **workspace** folder.

**Done! Now you can go to VS Code, Rhino, or Grasshopper to run the example files of CDF.**

First time using VS Code and on Windows? Make sure select the correct terminal profile: Ctrl+Shift+P, Terminal: Select Default Profile and select Command Prompt.
