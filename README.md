# Data Analytics and Science Environment 

### Technologies utilized here:
- Ansible
- Docker
- AWS S3
- Jupyter Notebooks
    - Saving Notebooks in S3: PIP package: *s3contents* {utilized to save filers, notebooks in bucket}
    - Viewing Notebooks easily: *COMMUTER*: javasript // {utilized to view-only --> existing notebooks }
        - NOTE - this package is `de-activated` as this function is covered by s3contents package (should keep eye out for releases)
    - Saving Notebook Alternative: *Bookstore* --> from nINTERACT group, not as good as s3contents for our purposes currently 
        - NOTE - this package is `de-activated` as this funciton is covered by s3contents package (should keep eye out for releases)

### STEP1: AWS IAM Configuration   
Before running ansible to generate EC2 instance, you will need to create/ensure there is a IAM role that can access the specific bucket that will contain the folders / items that the notebook will pull from. If there is not a existing IAM role, create one with permissions to do everything (Read, Write, Edit): with the name of 
`s3_datascience_policy_access`: 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "ec2:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::instagramcv//.s3keep"
        }
    ]
}
```

`Cautionary note --> should revise "ec2:*" permissions --> this grants permissions to EVERYTHING related to EC2 (creating, detorying, etc...) poses high risk`



### STEP 2: AWS S3 Configuration and AWS KEY-ACCESS/ID 
Before running the environment, a S3 bucket should be created to act as the 'file' repository. Once a new bucket 
has been created within S3, please go into `env_docker_compose\jupyter_config_files` and replace the s3 bucket name with the name of the 
bucket you would like to utilize. In addition, the `access_key_id` and `secret_access_key` should be replaced appropriately. 

NOTE - the user then has two permissions, the one above, in addition to the standard EC2 permissions: 
``` AmazonEC2ContainerRegistryFullAccess ``` 

So in my instance, it looks like this for the role: 
`s3_instagramcv_policy_access`
`AmazonEC2ContainerRegistryFullAccess`

### STEP 3: JUPYTER NOTEBOOK PASSWORD 
A fixed password is being utilized for testing purposes. This can be modified, turn on/off or changed within each of the 
appropriate config files `env_docker_compose\jupyter_config_files` and at the line level of `c.NotebookApp.token`

### STEP 4A: CREATE EC2 INSTANCE WITH ANSIBLE
To create a new EC2 instable, modify the name as needed, but all of this should be found within `ansible_create_ec2.yml` file.
You will then run this by using 
- `ansible-playbook ansible_create_ec2.yml` 

### STEP 4B: ADD NEWLY CREATED EC2 INSTANCE TO HOSTS FILE and SSH CONFIG FILE 
- `nano etc/ansible/hosts`
- `nano ~/.ssh/config`

### STEP 5: INSTALL DOCKER AND DOCKER-COMPOSE 
- For future reference, can combine these two ansible playbooks into single playbook
- You will then run this by using `ansible-playbook ansible_install_docker` 

### STEP 6: RUN DOCKER-COMPOSE
- You will then run this by using `ansible-playbook ansible_run_dockercompose` 





### FUTURE MODIFICATIONS REQUIRED FOR SECURITY: 
NOTE to self: will need to go back and change source code to jupyter notebook to disable downloads, looks like it lives in: 
`notebook/notebook/templates/notebook.html`
And would then want to comment out: 

```
                        <li class="dropdown-submenu" role="none"><a href="#" role="menuitem">{% trans %}Download as{% endtrans %}<span class="sr-only">{% trans %}Toggle Dropdown{% endtrans %}</span></a>
                            <ul id="download_menu" class="dropdown-menu">
                                {% for exporter in get_frontend_exporters() %}
                                <li id="download_{{ exporter.name }}">
                                    <a href="#">{{ exporter.display }}</a>
                                </li>
                                {% endfor %}
                            </ul>
                        </li>

```

