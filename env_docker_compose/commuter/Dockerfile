FROM jupyter/minimal-notebook:abdb27a6dfbb
RUN npm install @nteract/commuter -g

# Alternative way with YARN instead of NPM below: 
# USER root
# RUN apt-get update && apt-get install -y curl gnupg gnupg2 gnupg1
# RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
# RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
# RUN apt-get update && apt-get install --no-install-recommends yarn
# RUN yarn global add @nteract/commuter

