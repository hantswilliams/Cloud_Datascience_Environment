FROM jupyter/minimal-notebook:abdb27a6dfbb

RUN pip install jupyter_contrib_nbextensions
RUN pip install jupyter_nbextensions_configurator
RUN pip install s3contents --no-cache-dir

RUN jupyter notebook --generate-config -y
RUN jupyter contrib nbextension install --user 
RUN jupyter nbextensions_configurator enable --user

# ENABLING EXTENSIONS - OOB 
RUN jupyter nbextension enable varInspector/main
RUN jupyter nbextension enable snippets/main
RUN jupyter nbextension enable snippets_menu/main
RUN jupyter nbextension enable table_beautifier/main
RUN jupyter nbextension enable toc2/main

# ENABLING EXTENSIONS - CUSTOM  
COPY custom_jupyter_extensions/setup /opt/conda/lib/python3.7/site-packages/jupyter_contrib_nbextensions/nbextensions/setup
RUN jupyter contrib nbextensions install --user
RUN jupyter nbextension enable setup/main

# ENABLE S3 CONNECTION / CONFIG FILE FOR JUPYTER  
COPY jupyter_config_files/jupyter_notebook_config.py $HOME/.jupyter/jupyter_notebook_config.py

# CONFIGURE THE CONFIG FILE WITH PROPER AWS CREDENTIALS 
# Allow for ENV variables for Superset Parameters 
ARG AWS_KEYID  
ARG AWS_SECRET
ARG AWS_BUCKET
ARG NOTEBOOK_PASSWORD
RUN sed -i "/c.S3ContentsManager.access_key_id*/c\c.S3ContentsManager.access_key_id = $AWS_KEYID" $HOME/.jupyter/jupyter_notebook_config.py;
RUN sed -i "/c.S3ContentsManager.secret_access_key*/c\c.S3ContentsManager.secret_access_key = $AWS_SECRET" $HOME/.jupyter/jupyter_notebook_config.py;
RUN sed -i "/c.S3ContentsManager.bucket*/c\c.S3ContentsManager.bucket = $AWS_BUCKET" $HOME/.jupyter/jupyter_notebook_config.py;
RUN sed -i "/c.NotebookApp.token*/c\c.NotebookApp.token = $NOTEBOOK_PASSWORD" $HOME/.jupyter/jupyter_notebook_config.py;

# FOR BOOKSTORE / from nINTERACT 
# RUN pip install bookstore
# RUN jupyter serverextension enable --py bookstore
# COPY jupyter_config_files/jupyter_notebook_config_bookstore.py $HOME/.jupyter/jupyter_notebook_config.py




