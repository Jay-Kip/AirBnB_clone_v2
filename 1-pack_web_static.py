#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
"""

import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """

    time = datetime.now()
    ''' Create the archive name based on the current date and time'''
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    ''' Create versions folder if it doesnt already exist'''
    local('mkdir -p versions')

    ''' Create the archive using the tar command'''
    create = local('tar -cvzf versions/{} web_static'.format(archive))

    ''' Check if archive creation was successful'''
    if create is not None:
        return archive
    else:
        return None
