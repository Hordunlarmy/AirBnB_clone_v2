#!/usr/bin/python3
# a Fabric script (based on the file 1-pack_web_static.py)
from fabric.api import env, put, run
from datetime import datetime
from os import path


env.hosts = ['54.175.122.179', '100.26.230.33']
# env.user = 'ubuntu'


def do_deploy(archive_path):
    """ distributes an archive to your web servers """

    try:
        if not path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')
        filename = archive_path[9:-4]

        run(f'sudo mkdir -p /data/web_static/releases/{filename}/')
        run(f'sudo tar -xzf /tmp/{filename}.tgz -C \
                /data/web_static/releases/{filename}/')
        run(f'sudo rm /tmp/{filename}.tgz')
        run(f'sudo mv /data/web_static/releases/{filename}/web_static/* \
                /data/web_static/releases/{filename}/')
        run(f'sudo rm -rf /data/web_static/releases/{filename}/web_static')
        run(f'sudo rm -rf /data/web_static/current')
        run(f'sudo ln -sf /data/web_static/releases/{filename}/ \
                /data/web_static/current')

        print("New version deployed!")
        return True
    except Exception as e:
        return False
