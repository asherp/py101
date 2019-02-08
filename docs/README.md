# About

The Lab Materials are hosted on the developer nasa git here 
[https://developer.nasa.gov/CCMC/python101](https://developer.nasa.gov/CCMC/python101)

Where you will find

* python environment files
* python notebooks
* example python executables

# Installation

The cleanest and easiest way to get the requirements is to use the anaconda packaging and environment system. First navigate here:

[https://conda.io/miniconda.html](https://conda.io/miniconda.html
)

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

# Organization

These materials are organized into several different notebooks by topic:

* [Notebook Basics](notebooks/Notebook_basics.ipynb) - How to run and navigate the notebooks
* [Python Data types](notebooks/Python_Data_Types.ipynb) - covers python's built-in data types and operations (int, float, list, tuple, dict, etc.)
* [Scientific Data Types](notebooks/Scientific_Data_Types.ipynb) - covers numpy and pandas data and operations
* [Defining Functions](notebooks/Functions.ipynb) - how to write custom functions and decorators
* [Defining Types](notebooks/Custom_Types.ipynb) - how to write custom data types (objects)
* [File I/O](notebooks/File_IO.ipynb) - how to read and write files 
* [Executables](notebooks/Scripting.ipynb) - generating executable scripts
