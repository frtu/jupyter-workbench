#!/bin/sh
nginx -g 'daemon off;' &
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --notebook-dir=/notebooks --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.iopub_data_rate_limit='1.0e10' --no-browser
