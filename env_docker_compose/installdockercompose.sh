#!/bin/bash

# prep the system / install python manager - pyenv
yes | sudo apt-get update;
yes | sudo apt-get install build-essential;
yes | sudo apt-get install zlib1g-dev;
yes | sudo apt-get install libssl-dev libbz2-dev libreadline-dev libsqlite3-dev python3-dev;
# yes | sudo apt install -y python3-pip


# first install docker 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
yes | sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
yes | sudo apt-get update
apt-cache policy docker-ce
yes | sudo apt-get install -y docker-ce

# now install dockercompose 
yes | sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
yes | sudo chmod +x /usr/local/bin/docker-compose

# now confirm
docker --version
docker-compose --version

# now install python specific SDKs for docker 
# yes | pip3 install docker 

# this for changing, enabling python command to then run python3 
# echo 'alias python=python3' >> ~/.bashrc;
# source ~/.bashrc;


