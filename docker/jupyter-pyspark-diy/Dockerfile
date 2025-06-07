ARG VERSION=latest

FROM jupyter/base-notebook:${VERSION}

USER root
RUN apt-get update && apt-get install -y openjdk-11-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
USER $NB_USER

# Copy requirements into the image
COPY requirements.txt /tmp/requirements.txt

# Install requirements
RUN pip install --no-cache-dir -r /tmp/requirements.txt