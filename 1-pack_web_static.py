#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


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
        path = local("tar -cvzf {} web_static".format(filename))
        return path
    except Exception as e:
        return None
