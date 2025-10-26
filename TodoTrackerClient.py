import socket
import sys
from ClientCommands import (
    add_command,
    list_command,
    remove_command,
    mark_command,
    quit_command,
    unknown_command,
)


# connects to todo tracker server and processes commands from user input
def main():

    if len(sys.argv) != 3:
        print("Usage: python3 ToDoTracketClient.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    # keep receiving inputs from the client until they stop
    while True:
        # input line
        command = input()

        # map input commands to their functions
        if command == "ADD":
            add_command(sock)
        elif command == "LIST":
            list_command(sock)
        elif command == "REMOVE":
            remove_command(sock)
        elif command == "MARK":
            mark_command(sock)
        elif command == "QUIT":
            quit_command(sock)
        else:
            unknown_command(sock, command)


if __name__ == "__main__":
    main()
