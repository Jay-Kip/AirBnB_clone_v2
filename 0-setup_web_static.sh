#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
sudo apt-get update

# Install nginx
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create html file
sudo echo "<html>
  <head>
  </head>
  <body>
  Hello world ;)
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Change ownership
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart nginx
sudo service nginx restart
