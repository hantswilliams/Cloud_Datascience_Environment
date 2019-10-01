from s3contents import S3ContentsManager

c = get_config()

# Tell Jupyter to use S3ContentsManager for all storage.
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = "DYNAMICALLYINSERTED"
c.S3ContentsManager.secret_access_key = "DYNAMICALLYINSERTED" 
c.S3ContentsManager.bucket = "DYNAMICALLYINSERTED"
c.NotebookApp.token = "DYNAMICALLYINSERTED"