#!/usr/bin/python3
# a Fabric script
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions/')
    output = local('tar -cvzf {} web_static/'.format(file_path))

    if output.succeeded:
        file_size = os.path.getsize(file_path)
        print(f"web_static packed: {file_path} -> {file_size}Bytes")
        return file_path
