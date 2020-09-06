# jupyter-workbench
Workbench for jupyter notebook

## Docker

Under **docker/jupyter-data-science**, find :

* **requirements.txt** : All python libraries for pre-installation
* **jupyter docker** : build image with pre-installed python lib using base image : ```continuumio/anaconda3:2020.07```
* **docker-compose** : starting and building that image
* **build.bash** : to build image and name it ```jupyter-data-science:2020-09```

## Notebooks

### Crawler

* **Crawler class** : notebooks/libs/crawler-class.ipynb
* Returning **BeautifulSoup** objects


Import using :

```
%run /notebooks/local/libs/crawler-class.ipynb

crawler = Crawler(BASE_URL)
soup = crawler.parseUrl(BASE_URL, False)
```