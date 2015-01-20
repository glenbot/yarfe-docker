FROM ubuntu:14.04
MAINTAINER Glen Zangirolami

# Install base packages required to run all python packages
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev python-pip

# Install requirements from packages by copying the 
# requirements.pip file over first for optimal docker
# caching
ADD yarfe/requirements.pip /var/code/yarfe/requirements.pip
RUN pip install -r /var/code/yarfe/requirements.pip

# Add the pth file
ADD yarfe.pth /usr/local/lib/python2.7/dist-packages/yarfe.pth

# Add the rest of the code
ADD yarfe /var/code/yarfe
