#!/usr/bin/python3

from fabric import task
from fabric import Connection
from datetime import datetime


@task   # This eniables the function to be executed remotely
def do_pack(c):
    ''' Create the versions folder if it does not exist'''
    c.run('mkdir -p versions')

    # Generate timestamp for the archive name
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # Create the archive file
    archive_name = f'web_static_{timestamp}.tgz'
    c.run(f'tar -czvf versions/{archive_name} web_static')

    # Return the path of the generated archive
    return f'version/{archive_name}'
