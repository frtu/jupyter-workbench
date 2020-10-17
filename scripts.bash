echo "Type 'startjdatascience' to start jupyter-data-science-py"
startjdatascience() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-data-science-py && exec docker-compose up)
}
echo "Type 'startjocr' to start jupyter-ocr-tesseact-py"
startjocr() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-ocr-tesseact-py && exec docker-compose up)
}
echo "Type 'startjspark' to start jupyter-sparkmagic"
startjspark() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-sparkmagic && exec docker-compose up)
}
echo "Type 'startpyspark' to start jupyter-pyspark"
startpyspark() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-pyspark && exec docker-compose up)
}

