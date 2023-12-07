#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    a Fabric script that generates a .tgz archive from the contents of
    the web_static
    """
    try:
        now = datetime.now()
        filename = "web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S")
        )
        local("mkdir versions")
        path = local(f"tar -cvzf {filename} web_static")
        return path
    except Exception as e:
        return None
