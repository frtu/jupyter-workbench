# jupyter-workbench
Workbench for jupyter notebook

## Docker

Under **docker/jupyter-data-science**, find :

* **requirements.txt** : All required python libraries
* **jupyter docker** image with requirements using base image : ```continuumio/anaconda3:2020.07```
* **docker-compose** : starting and building that image
* **build.bash** : to build image and name it ```jupyter-data-science:2020-09```