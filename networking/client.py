import socket
import sys  # for exit

HOST = '127.0.0.1'
PORT = 8910

# Create Socket
try:
    # AF_INET - IPv4, SOCK_STREAM - TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket.')
    sys.exit()
else:
    print('Socket created')

# Connect to server
try:
    sock.connect((HOST, PORT))
except socket.error:
    print('Connection to server failed')
    sys.exit()
else:
    print('Connected to {0}:{1}'.format(HOST, PORT))
    reply = sock.recv(4096)  # Connection confirmation message
    print("Response: ", reply.decode('UTF-8'))

while True:
    # Send some data to remote server
    command = input("Command: ")

    try:
        # Set the whole string
        sock.sendall(command.encode('UTF-8'))
    except socket.error:
        # Send failed
        print('Send failed')
        sys.exit()
    else:
        print('Send successfully')

    # Now receive data
    reply = sock.recv(4096)

    print("Response:", reply.decode('UTF-8'), "\n")
