import socket
import sys
from thread import ClientThread

HOST = '127.0.0.1'    # Localhost
PORT = 8910  # Any port which requires general privileges

# Create Socket
try:
    # AF_INET - IPv4, SOCK_STREAM - TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket.')
    sys.exit()
else:
    print('Socket created')

# Bind socket to host and port
try:
    sock.bind((HOST, PORT))
except socket.error:
    print('Bind failed.')
    sys.exit()
else:
    print('Socket bind complete')

# Start listening on socket
sock.listen(10)
print('Socket now listening')

# Keep talking with the client
while True:
    # blocking while accept a connection
    conn, addr = sock.accept()
    print('Connected with {0}:{1} addr: {2}'.format(addr[0], PORT, str(addr[1])))

    # start new thread
    t = ClientThread(conn)
    t.start()

sock.close()
