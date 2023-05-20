echo "Type 'startllm' to start jupyter-llm"
startllm() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-llm && exec docker-compose up)
}
echo "Type 'startpyspark' to start jupyter-pyspark"
startpyspark() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-pyspark && exec docker-compose up)
}
echo "Type 'startjspark' to start jupyter-sparkmagic"
startjspark() {
  echo "Make sure you have ** docker-compose ** installed !!"
  (cd docker/jupyter-sparkmagic && exec docker-compose up)
}
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


echo "Type 'builddocker' to build"
builddocker() {
  echo "Usage : builddocker [IMAGE_NAME|docker-parameters] [SIMPLE_ARG] [DEFAULT_TEXT]"

  local IMAGE_NAME=${1:-docker-parameters}
  local SIMPLE_ARG=$2
  local DEFAULT_TEXT=$3

  # Remove intermediate layer & no relying on built cache
  local EXTRA_PARAMS="--force-rm=true --no-cache=true"
  if [ -n "SIMPLE_ARG" ]; then
    local EXTRA_PARAMS="${EXTRA_PARAMS} --build-arg SIMPLE_ARG=${SIMPLE_ARG}"
  fi
  if [ -n "DEFAULT_TEXT" ]; then
    local EXTRA_PARAMS="${EXTRA_PARAMS} --build-arg DEFAULT_TEXT=${DEFAULT_TEXT}"
  fi

  echo "docker build -t ${IMAGE_NAME} ${VARIABLE_NAME} ${EXTRA_PARAMS} -f Dockerfile.env ."
  docker build -t ${IMAGE_NAME} ${VARIABLE_NAME} ${EXTRA_PARAMS} -f Dockerfile.env .
}

echo "Type 'rundocker' to run"
rundocker() {
  echo "Usage : rundocker [IMAGE_NAME|docker-parameters] [SIMPLE_ARG] [DEFAULT_TEXT] [CMD]"

  local IMAGE_NAME=${1:-docker-parameters}
  local SIMPLE_ARG=$2
  local DEFAULT_TEXT=$3
  local EXTRA_ARGUMENTS=${@:4}

  if [ -n "SIMPLE_ARG" ]; then
    local EXTRA_PARAMS="${EXTRA_PARAMS} --env SIMPLE_ARG=${SIMPLE_ARG}"
  fi
  if [ -n "DEFAULT_TEXT" ]; then
    local EXTRA_PARAMS="${EXTRA_PARAMS} --env DEFAULT_TEXT=${DEFAULT_TEXT}"
  fi

  echo "docker run ${EXTRA_PARAMS} ${IMAGE_NAME}:latest ${EXTRA_ARGUMENTS}"
  docker run ${EXTRA_PARAMS} ${IMAGE_NAME}:latest ${EXTRA_ARGUMENTS}
}

echo "Type 'runcompose' to run"
runcompose() {
  echo "docker-compose up --force-recreate"
  docker-compose up --force-recreate
}