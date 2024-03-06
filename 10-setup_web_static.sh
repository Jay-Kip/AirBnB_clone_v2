#!/usr/bin/ env bash
# Bash script that sets up your web servers for the deployment of web_static.

#install nginx
sudo apt install nginx

#create folder data
mkdir /data/

mkdir /data/web_static/

mkdir /data/web_static/releases/

mkdir /data/web_static/shared/

mkdir /data/web_static/releases/test/

echo "Hello world!!" >> /data/web_static/releases/test/index.html/
