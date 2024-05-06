#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """
    try:
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

    return Nonei
