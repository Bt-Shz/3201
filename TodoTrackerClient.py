import socket
import sys
from ClientCommandHandles import (
    handle_add,
    handle_list,
    handle_remove,
    handle_mark,
    handle_quit,
    handle_unknown_command,
)


def main():
       
    if len(sys.argv) != 3:
        print("Usage: python3 ToDoTracketClient.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        
        sock.connect((server_ip, server_port))

        
        while True:
            
            command = input().strip().upper()  

            
            if command == "ADD":
                handle_add(sock)
            elif command == "LIST":
                handle_list(sock)
            elif command == "REMOVE":
                handle_remove(sock)
            elif command == "MARK":
                handle_mark(sock)
            elif command == "QUIT":
                handle_quit(sock)
            else:
                
                handle_unknown_command(sock, command)

    except ConnectionError as e:
        print(f"Connection error: {e}")
        sock.close()
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nClient interrupted. Closing connection...")
        sock.close()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sock.close()
        sys.exit(1)


if __name__ == "__main__":
    main()
