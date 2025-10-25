
def read_line(sock):
    """
    Read a line from the socket until '\n' is encountered.
    Returns the line as a string (without '\n').
    """
    line = b""
    while True:
        chunk = sock.recv(1)
        if not chunk:
            raise ConnectionError("Connection closed by server")
        line += chunk
        if chunk == b"\n":
            break
    return line.decode("utf-8").strip()


def read_until_hash(sock):
    """
    Read lines from the socket until '
    Returns a list of lines (without the '
    """
    lines = []
    while True:
        line = read_line(sock)
        if line == "
            break
        lines.append(line)
    return lines


