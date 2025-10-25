import socket
import sys
from ReadLineFunctions import read_line, read_until_hash

def handle_add(sock):
    send_command(sock, "ADD")

    
    while True:
        line = input()
        send_command(sock, line)
        if line == "
            break

    
    response = read_line(sock)
    print(response)


def handle_list(sock):
    """
    Receive and display all tasks from server.
    """
    send_command(sock, "LIST")

    
    lines = read_until_hash(sock)
    for line in lines:
        print(line)


def handle_remove(sock):
    
    send_command(sock, "REMOVE")

    
    while True:
        line = input()
        send_command(sock, line)
        if line == "
            break

    
    response = read_line(sock)
    print(response)


def handle_mark(sock):
   
    send_command(sock, "MARK")

    
    while True:
        line = input()
        send_command(sock, line)
        if line == "
            break

    
    response = read_line(sock)
    print(response)


def handle_quit(sock):
    send_command(sock, "QUIT")

    
    response = read_line(sock)
    print(response)

    
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

    
    sys.exit(0)


def handle_unknown_command(sock, command):
    send_command(sock, command)

    
    response = read_line(sock)
    print(response)




def send_command(sock, command):
    sock.send((command + "\n").encode("utf-8"))



