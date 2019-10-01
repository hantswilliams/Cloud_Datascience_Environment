FROM jupyter/minimal-notebook:abdb27a6dfbb
RUN jupyter notebook --generate-config -y
COPY jupyter_config_files/jupyter_notebook_config_lab.py $HOME/.jupyter/jupyter_notebook_config.py

ARG NOTEBOOK_PASSWORD
RUN sed -i "/c.NotebookApp.token*/c\c.NotebookApp.token = $NOTEBOOK_PASSWORD" $HOME/.jupyter/jupyter_notebook_config.py;







