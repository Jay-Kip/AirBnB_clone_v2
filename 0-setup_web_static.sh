#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.


# install nginx iif i does not exist

if !	command -v nginx &> /dev/null;	then
	apt-get update
	apt-get -y install nginx
fi

# Create folders if they dont exist

mkdir -p /data/web_static/{releases/test,shared}

# Create test HTML file

echo "Hello world!" > /data/web_static/releases/test/index.html

# Create or recreate a symbolic link

if [	-L /data/web_static/current	];	then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group recursively

chown -R ubuntu:ubuntu /data/

# Update nginx

config_file="/etc/nginx/sites-available/default"

# Remove existing config from hbnb_static if it exists

sed -i '/location \/hbnb_static {/,/}/d'	config_file

# Add new config file for hbnb_static

echo "
	location /hbnb_tatic {
	alias /data/web_static/current/;
	index index.html;
}
" >> $config_file

# Restart nginx

service nginx restart
