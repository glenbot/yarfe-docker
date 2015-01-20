

def read_socket_data(socket, multipart=False, flags=0):
    """Read socket data using ZMQ sockets

    :param socket: the ZMQ socket to read data from
    """
    if multipart:
        return socket.recv_multipart(flags=flags)
    return socket.recv_pyobj(flags=flags)


def write_socket_data(socket, data, multipart=False, flags=0):
    """Write socket data using ZMQ sockets

    :param data: the python object to send down the socket
    :param bool multipart: send the data as socket.multipart
    """
    if multipart:
        socket.send_multipart(data, flags=flags)
    else:
        socket.send_pyobj(data, flags=flags)
