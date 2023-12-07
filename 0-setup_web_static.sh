#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<h1>Hello World</h1>" > /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static {/n/t/t alias /data/web_static/current/;/n}' /etc/nginx/sites-available/hordun.tech
sudo service nginx restart
