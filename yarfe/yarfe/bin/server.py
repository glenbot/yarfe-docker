#!/usr/bin/env python
"""
YARFE - Yet another remote file explorer. A sample application
to show how to deploy Python applications in Docker.

Usage:
    yarfe-server [options]

Options:

    --address=<address>  The address to serve data on [default: 127.0.0.1].
    --port=<port>  The port to data on [default: 9000].
    --path=<path>  Path to serve data from [default: /tmp]
    --help  Show this screen.
"""
# to patch threading correctly gevent must be loaded first
import gevent
from gevent.monkey import patch_all

# patch all gevent processes
patch_all()

import os
import subprocess
from docopt import docopt
import zmq.green as zmq

from ..utils import read_socket_data, write_socket_data

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
AVAILABLE_COMMANDS = [
    'HELP',
    'LIST',
    'CAT',
    'MOTD'
]


def handler(socket, path):
    """Handle a socket connection"""
    while True:
        command = None
        param = None
        data = read_socket_data(socket)

        # parse out the command
        if 'CMD' in data:
            keys = data.split()
            if len(keys) == 2:
                command = keys[1]
            elif len(keys) == 3:
                command, param = keys[1], keys[2]

        if command not in AVAILABLE_COMMANDS:
            write_socket_data(socket, 'Command not found.')
            continue
           
        if command is None:
            write_socket_data(socket, 'Command not found.')
            continue

        if command == 'LIST':
            output = subprocess.check_output(
                "cd {} && ls -al".format(path),
                shell=True
            )
        elif command == 'MOTD':
            with open(os.path.join(PROJECT_ROOT, 'motd.txt'), 'r') as f:
                output = f.read()
        elif command == 'HELP':
            _help = [
                'HELP - Show list of commands',
                'MOTD - Show the message of the day',
                'LIST - List directory contents',
                'CAT  - Show file contents'
            ]
            output = '\n'.join(_help)
        elif command == 'CAT':
            if not os.path.isfile(os.path.join(path, param)):
                output = 'File not found.'
            else:
                output = subprocess.check_output(
                    "cd {} && cat {}".format(path, param),
                    shell=True
                )

        write_socket_data(socket, output)


def main():
    # parse the options from the CLI
    options = docopt(__doc__)

    # get a ZMQ context and start a REP/REQ socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)

    def _server(_socket, path):
        _socket.bind('tcp://{--address}:{--port}'.format(**options))
        handler(socket, path)

    # Start the server
    print('Server started on {--address}:{--port}'.format(**options))
    gevent.joinall([gevent.spawn(_server, socket, options['--path'])])


if __name__ == '__main__':
    main()
