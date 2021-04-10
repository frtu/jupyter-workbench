# https://hub.docker.com/r/continuumio/anaconda3/tags
ARG BASE_CONTAINER=continuumio/anaconda3:2020.07
FROM $BASE_CONTAINER

USER root

ENV NB_PREFIX /

# Creating directories
RUN mkdir -p /data /notebooks/local

# Setting up volumes
VOLUME ["/data", "/notebooks/local"]

#Set working directory
# WORKDIR /notebooks

COPY requirements.txt /notebooks/requirements.txt
RUN pip install --upgrade pip && pip install -r /notebooks/requirements.txt

# jupyter
EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--notebook-dir=/notebooks", "--NotebookApp.token=''", "--NotebookApp.password=''",  --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}, "--no-browser"]
