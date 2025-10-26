import socket
import sys
from ClientReadLine import read_line, read_until_hash


# this file contains all the commands that client runs
# each command sends appropriate data to server and reads response


# sends ADD command to server with task details, then prints server response
def add_command(sock):
    send_command(sock, "ADD")

    while True:
        line = input()
        send_command(sock, line)
        if line == "":
            break

    response = read_line(sock)
    print(response)


# sends LIST command to server, then reads and prints all tasks until `#`
def list_command(sock):
    send_command(sock, "LIST")
    lines = read_until_hash(sock)
    for line in lines:
        print(line)


# sends REMOVE command to server with task ID, then prints server response
def remove_command(sock):
    send_command(sock, "REMOVE")

    while True:
        line = input()
        send_command(sock, line)
        if line == "":
            break

    response = read_line(sock)
    print(response)


# sends MARK command to server with task ID, then prints server response
def mark_command(sock):
    send_command(sock, "MARK")

    while True:
        line = input()
        send_command(sock, line)
        if line == "":
            break

    response = read_line(sock)
    print(response)


# sends QUIT command to server, prints response, then closes socket and exits
def quit_command(sock):
    send_command(sock, "QUIT")
    response = read_line(sock)
    print(response)

    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    sys.exit(0)


# sends unknown command to server and prints error response
def unknown_command(sock, command):
    send_command(sock, command)
    response = read_line(sock)
    print(response)


# sends command string to socket `sock` with newline terminator
def send_command(sock, command):
    sock.send((command + "\n").encode("utf-8"))
