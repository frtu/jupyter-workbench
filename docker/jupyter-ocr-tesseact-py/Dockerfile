FROM ocrd/tesserocr:latest

# Creating directories
RUN mkdir -p /data /notebooks/local

# Setting up volumes
VOLUME ["/data", "/notebooks/local"]

#Set working directory
# WORKDIR /notebooks

#RUN apt update && apt install -y python3-pip
RUN pip3 install jupyterlab notebook pillow pytesseract

# jupyter
EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--notebook-dir=/notebooks", "--no-browser"]
