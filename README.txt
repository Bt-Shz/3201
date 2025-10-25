TodoTrackerClient - README
==========================

DEVELOPMENT ENVIRONMENT
-----------------------
Language: Python 3
Operating System: Linux (Ubuntu/Debian-based)
Required: Python 3.6 or higher

COMPILATION
-----------
No compilation needed (Python is interpreted).

HOW TO RUN
----------
1. First, start the server in one terminal:
   python3 TodoTrackerServer.py

2. Then, in another terminal, run the client:
   python3 ToDoTracketClient.py <server_ip> <server_port>

   Example:
   python3 ToDoTracketClient.py 127.0.0.1 18222

USAGE
-----
After connecting to the server, you can use the following commands:

1. ADD - Add a new task
   - Type: ADD
   - Then enter task description (multiple lines allowed)
   - End with: #
   
   Example:
   ADD
   Buy groceries
   Milk and eggs.
   #

2. LIST - View all tasks
   - Type: LIST
   - Server will display all tasks

3. REMOVE - Remove tasks by ID
   - Type: REMOVE
   - Then enter task IDs (one per line)
   - End with: #
   
   Example:
   REMOVE
   0000
   0001
   #

4. MARK - Toggle task status (pending ↔ completed)
   - Type: MARK
   - Then enter task IDs (one per line)
   - End with: #
   
   Example:
   MARK
   0000
   #

5. QUIT - Exit the client
   - Type: QUIT
   - Client will disconnect and exit

FEATURES IMPLEMENTED
--------------------
✓ Socket initialization (Task 1)
✓ Connection to server with IP and port from command-line arguments (Task 2)
✓ ADD command - sends multi-line task descriptions (Task 3)
✓ LIST command - receives and displays all tasks (Task 3 & 4)
✓ REMOVE command - sends task IDs for removal (Task 3 & 4)
✓ MARK command - sends task IDs for status toggle (Task 3 & 4)
✓ QUIT command - properly closes connection (Task 3, 4 & 5)
✓ Error handling for invalid commands and connection issues
✓ Proper newline character handling ('\n' appended to all messages)

CODE STRUCTURE
--------------
- read_line(): Reads one line from socket
- read_until_hash(): Reads multiple lines until '#' marker
- send_command(): Sends a command with proper formatting
- handle_add(): Handles ADD command logic
- handle_list(): Handles LIST command logic
- handle_remove(): Handles REMOVE command logic
- handle_mark(): Handles MARK command logic
- handle_quit(): Handles QUIT command and cleanup
- handle_unknown_command(): Handles unrecognized commands
- main(): Main program loop with socket initialization and command processing

ERROR HANDLING
--------------
- Connection errors are caught and reported
- Server disconnections are detected
- Invalid commands are sent to server for error response
- Keyboard interrupts (Ctrl+C) are handled gracefully

NOTES
-----
- All commands are case-insensitive (converted to uppercase)
- All messages sent to server include '\n' character
- Socket is properly closed using shutdown() and close()
- Program exits cleanly after QUIT command
