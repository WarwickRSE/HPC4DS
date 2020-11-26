# What are these files

These files show a simple example of a singularity container definition file.

This creates a Singularity container to run an image blurring program based on
the ImageBlur Notebook. We exported to a script and added the ability to take
a command line parameter. The resulting script is in this directory.

The setup process for this container has to:
* Start from an Ubuntu image on Dockerhub for the base OS
* Copy in the script file ImageBlur.py
* Inside the container, provision it with Python and the packages we need
* When the container runs, take a parameter telling it what image file to operate on
* Run the script

Remember that build the container you will need to run Singularity as root, for example
`sudo singularity build <sif\_file.sif> ImageBlur\_Singularity\_Definition` where <sif\_file.sif>
shoud be replaced with the name you want the container to have. 

Note: you can use online services to build containers, such as [this](https://cloud.sylabs.io/builder). 
We don't cover this here in detail, but do note you will need to get an account
and generate a token to use it.

