#!/usr/bin/python3
# a Fabric script
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    try:
        now = datetime.now()
        filename = "web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S")
        )
        local("mkdir versions")
        path = local(f"tar -cvzf versions/{filename} web_static")
        file_path = f"versions/{filename}"
        file_size = os.path.getsize(file_path)
        print(f"web_static packed: versions/{filename} -> {file_size}Bytes")
        return file_path
    except Exception as e:
        return None
