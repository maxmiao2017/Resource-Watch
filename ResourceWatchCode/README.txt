This repository contains code for the Resource Watch project. It is organized
in 5 sections:

* API Educational Materials
* Data Access Assistance
* Metadata Management
* Notebooks for Exploring Specific Datasets
* Raster Dataset Processing

~~~

The python code depends on several other code libraries. To install the needed
dependencies, run "pip install -r requirements.txt" from your terminal
while in this folder.

If you encounter a problem, see this article:
* https://stackoverflow.com/questions/41457612/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project

If you have a problem installing rasterio, see this article:
* https://github.com/mapbox/rasterio/blob/master/docs/installation.rst

Many of these files are iPython jupyter notebooks (extension: .ipynb). In order
to run these, you will need to install jupyter on your computer. Then, from your
command line, you will run "jupyter notebook" in the folder you wish to explore
to view and edit the iPython notebooks.
* http://jupyter.readthedocs.io/en/latest/install.html
* http://jupyter.readthedocs.io/en/latest/running.html#running

~~~

In order to run terminal commands that begin with "aws", you will need
the AWS command line interface. Instructions for how to install and initialize
the AWS CLI are here:
* http://docs.aws.amazon.com/cli/latest/userguide/installing.html
* http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

~

In order to run terminal commands that begin with gcloud or gsutil, you will
need to install the Google Cloud SDK. Instructions for how to install and
initialize the Google Cloud SDK are here:
* https://cloud.google.com/sdk/docs/
* https://cloud.google.com/sdk/docs/initializing

~

In order to run terminal commands that begin with earthengine, you will need
to install the earthengine python libraries.

In your terminal, run:
pip install google-api-python-client
pip install earthengine-api
earthengine authenticate

~~~

Several terminal commands in this notebook rely on using variables from the
command line. There are different conventions for doing so when using
Linux or Windows based operating systems.

Ex. Linux (from ipython notebook) uses a single ($) symbol to invoke a variable value:
import os
os.environ["var_a"] = "hello"
!echo $var_a

Ex. Windows (from ipython notebook) uses two (%) symbols to invoke a variable value:
import os
os.environ["var_a"] = "hello"
!echo %var_a%

~~~

For an explanation of how to get started using Docker and Amazon Web Services,
see the walkthrough provided by Rutger Hofste:
* https://github.com/wri/Aqueduct30Docker
* https://hub.docker.com/r/rutgerhofste/gisdocker/
Included here are instructions of how to setup docker on your personal computer,
and instructions for how to set up an AWS cloud computing instance and load
code from GitHub onto it.

Rutger also provides some guidance on how to use Google Earth Engine code to
analyze raster datasets.

~~~

Useful repos to follow:
Resource Watch Notebooks: https://github.com/resource-watch/notebooks/tree/master/ResourceWatch
Vizzuality Data Science: https://github.com/Vizzuality/data_sci_tutorials
