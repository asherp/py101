# About

This repository hosts materials for the ccmc python/kamodo workshop. Here you will find

* python environment files
* python notebooks
* example python executables

# Installation

The cleanest and easiest way to get the requirements is to use the anaconda packaging and environment system. First navigate here:

https://conda.io/miniconda.html

Then download either python 2.7 or python 3. Both should work for these examples. When you run the installer, you'll have the option to choose the install path. You'll also choose whether to make this the default python interpreter. You can always edit your bashrc file to change this behavior.

## Tutorial materials
Clone this repository
    
    git clone git@developer.nasa.gov:CCMC/python101.git
    cd python101

Create and activate a new python 101 environment:

    conda create -n py101 python=3
    source activate py101

This last command activates the new environment so that your command prompt will be prepended with (py101)

## Requirements
The main packages needed for this tutorial are the following:

* jupyter
* numpy
* pandas
* click

However, each of these have several dependencies which must also be installed in our environment. To get all requirements:

    (py101) pip install -r requirements.txt

