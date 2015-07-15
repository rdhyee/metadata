FROM ubuntu:precise

# installing Python on ubuntu

RUN \
  apt-get update --fix-missing
  
# add repo for latest python
RUN \
  apt-get install -y python-software-properties
  
RUN \
  add-apt-repository ppa:fkrull/deadsnakes-python2.7

# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv
  
  
RUN \
  rm -rf /var/lib/apt/lists/*
    
# copy over the repo

COPY ./* /metadata/

# install requirements
  
RUN \
  pip install \
    pymarc==3.0.3 \
    rdflib==4.2.0 \
    PyYAML==3.11 \
    rdflib-jsonld==0.3

# add / to PYTHONPATH

ENV PYTHONPATH /:$PYTHONPATH

# Define working directory.
VOLUME ["/data"]

# Define default command.
CMD ["bash"]
