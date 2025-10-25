import socket
import sys
from ReadLineFunctions import read_line, read_until_hash
def handle_add(sock):
    """
    Read multi-line input from user until '#' is entered.
    """
    send_command(sock, "ADD")

    # Read task description from user
    while True:
        line = input()
        send_command(sock, line)
        if line == "#":
            break

    # Receive response from server
    response = read_line(sock)
    print(response)


def handle_list(sock):
    """
    Handle the LIST command.
    Receive and display all tasks from server.
    """
    send_command(sock, "LIST")

    # Read all lines until '#' is received
    lines = read_until_hash(sock)
    for line in lines:
        print(line)


def handle_remove(sock):
    """
    Handle the REMOVE command.
    Read task IDs from user until '#' is entered.
    """
    send_command(sock, "REMOVE")

    # Read task IDs from user
    while True:
        line = input()
        send_command(sock, line)
        if line == "#":
            break

    # Receive response from server
    response = read_line(sock)
    print(response)


def handle_mark(sock):
    """
    Handle the MARK command.
    Read task IDs from user until '#' is entered.
    """
    send_command(sock, "MARK")

    # Read task IDs from user
    while True:
        line = input()
        send_command(sock, line)
        if line == "#":
            break

    # Receive response from server
    response = read_line(sock)
    print(response)


def handle_quit(sock):
    """
    Handle the QUIT command.
    Send QUIT to server, receive OK, then close connection.
    """
    send_command(sock, "QUIT")

    # Receive response from server
    response = read_line(sock)
    print(response)

    # Close the socket
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

    # Exit the program
    sys.exit(0)
def handle_unknown_command(sock, command):
    """
    Handle unknown commands.
    Send the command to server and receive error message.
    """
    send_command(sock, command)

    # Receive error response from server
    response = read_line(sock)
    print(response)



def send_command(sock, command):
    """
    Send a command to the server.
    Automatically appends '\n' to the command.
    """
    sock.send((command + "\n").encode("utf-8"))



