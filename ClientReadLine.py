# this file contains all helper functions that read data from socket


# reads line from socket `sock` until `\n`. Then, returns that line as a string.
def read_line(sock):
    line = b""
    while True:
        chunk = sock.recv(1)
        if not chunk:
            raise ConnectionError("Connection closed by server")
        line += chunk
        if chunk == b"\n":
            break
    return line.decode("utf-8").strip()


# reads lines from socket `sock` until `#`. Then, returns a list of those lines as list of strings.
def read_until_hash(sock):
    lines = []
    while True:
        line = read_line(sock)
        if line == "#":
            break
        lines.append(line)
    return lines
