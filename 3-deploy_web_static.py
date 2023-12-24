#!/usr/bin/python3
# a Fabric script (based on the file 2-do_deploy_web_static.py) that creates
# and distributes an archive to your web servers
from fabric.api import env, put, run, local
from datetime import datetime
from os import path


env.hosts = ['54.175.122.179', '100.26.230.33']
# env.user = 'ubuntu'


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions/')
    output = local('tar -cvzf {} web_static/'.format(file_path))

    if output.succeeded:
        file_size = path.getsize(file_path)
        print(f"web_static packed: {file_path} -> {file_size}Bytes")
        return file_path


def do_deploy(archive_path):
    """ distributes an archive to your web servers """

    try:
        if not path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')
        filename = path.basename(archive_path)[:-4]

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


archive_path = do_pack()


def deploy():
    """Creates archive then distributes it to a web server."""
    if archive_path is None:
        return False
    return do_deploy(archive_path)
