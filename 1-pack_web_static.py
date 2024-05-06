#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    try:
        """Create the versions folder if it doesn't exist"""
        if not os.path.exists("versions"):
            os.makedirs("versions")

        """ Generate the archive path"""
        now = datetime.now()
        archive_name = "web_static_{} {} {} {} {} {}.tgz".format{
                now.year, now.month, now.day, now.hour, now.minute, now.second
                }
        archive_path = "versions/{}".format(archive_name)

        """Create the .tgz archive using the tar command"""
        local("tar -czvf {} web_statiic".format(archive_path))

        """ Return the archive path if the archive has been generated"""
        if os.path.exists(archive_path):
            return archive_path

    except Exception as e:
        print("An error occured during archive creation:", str(e))

    return None

    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
        """
