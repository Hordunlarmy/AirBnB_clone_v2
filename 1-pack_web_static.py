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
        filename = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
        local("mkdir -p versions")
        path = local(f"tar -czvf versions/{filename} web_static/")

        return path

    except Exception as e:
        return None
