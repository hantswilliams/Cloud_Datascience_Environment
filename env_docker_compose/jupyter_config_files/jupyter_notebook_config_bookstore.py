from bookstore import BookstoreContentsArchiver

c = get_config()

c.NotebookApp.contents_manager_class = BookstoreContentsArchiver

# All Bookstore settings are centralized on one config object so you don't have to configure it for each class
c.BookstoreSettings.workspace_prefix = "/workspace/datascience/notebooks"
c.BookstoreSettings.published_prefix = "/published/datascience/notebooks"

c.BookstoreSettings.s3_bucket = NEEDTOUPDATEINFUTURECURRENTLYNOTBEINGUTILIZED

# Note: if bookstore is used from an EC2 instance with the right IAM role, you don't
# have to specify these
c.BookstoreSettings.s3_access_key_id = NEEDTOUPDATEINFUTURECURRENTLYNOTBEINGUTILIZED 
c.BookstoreSettings.s3_secret_access_key = NEEDTOUPDATEINFUTURECURRENTLYNOTBEINGUTILIZED

c.NotebookApp.token = NEEDTOUPDATEINFUTURECURRENTLYNOTBEINGUTILIZED