ARG BASE_CONTAINER=jupyter/pyspark-notebook:latest
FROM $BASE_CONTAINER

USER root

# Creating directories
RUN mkdir -p /data /notebooks/local

# Setting up volumes
VOLUME ["/data", "/notebooks/local"]

#Set working directory
# WORKDIR /notebooks

# UNCOMMENT FOR CN
# RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list
# RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list
# RUN sed -i "s/security.debian.org/mirrors.aliyun.com\/debian-security/g" /etc/apt/sources.list

RUN sudo apt update 
RUN sudo apt -y install nginx

# https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-docker/
COPY ./nginx/conf /etc/nginx/

ADD ./nginx/reverse_proxy_start_up.sh /
RUN chmod +x /reverse_proxy_start_up.sh

# Forward request logs to Docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

STOPSIGNAL SIGTERM

# jupyter
EXPOSE 80 8888

ENTRYPOINT ["/bin/bash", "/reverse_proxy_start_up.sh"]
# ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--notebook-dir=/notebooks", "--no-browser"]
