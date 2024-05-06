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

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
