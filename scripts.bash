echo "Type 'startjdatascience' to start jupyter-data-science-py"
startjdatascience() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-data-science-py && exec docker-compose up)
}
echo "Type 'startjspark' to start jupyter-sparkmagic"
startjspark() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-sparkmagic && exec docker-compose up)
}
