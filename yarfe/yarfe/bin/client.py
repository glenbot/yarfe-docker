#!/usr/bin/env python
"""
YARFE - Yet another remote file explorer. A sample application
to show how to deploy Python applications in Docker.

Usage:
    yarfe-client [options]

Options:

    --address=<address>  The address to serve data on [default: 127.0.0.1].
    --port=<port>  The port to data on [default: 9000].
    --help  Show this screen.
"""
import zmq
from docopt import docopt

from ..utils import read_socket_data, write_socket_data


class Client(object):
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.fqdn = 'tcp://{}:{}'.format(self.address, self.port)
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connect(self):
        self.socket.connect(self.fqdn)

    def disconnect(self):
        # disconnect from the socket
        self.socket.disconnect(self.fqdn)

        # close and terminate buffer
        self.socket.close()

        # terminate the context
        self.context.term()

    def _format_command(self, command):
        return 'CMD {}'.format(command)

    def send(self, command):
        write_socket_data(self.socket, self._format_command(command))
        return read_socket_data(self.socket)


def main():
    # parse the options from the CLI
    options = docopt(__doc__)

    # connect to the client and send MOTD
    client = Client(options['--address'], options['--port'])
    client.connect()
    motd = client.send('MOTD')

    # print the motd
    print(motd)

    try:
        while True:
            command = raw_input('>> ')
            output = client.send(command)
            print(output)
    except KeyboardInterrupt:
        client.disconnect()
        print('Disconnected.')


if __name__ == '__main__':
    main()
