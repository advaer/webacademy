import threading
from processing import ClientProcessing

class ClientThread(threading.Thread):
    """
    New Thread for each Client
    """
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        self.connection.send('Welcome to the server. Ready to accept commands.\n'.encode('UTF-8'))
        client = ClientProcessing()
        while True:
            # Receiving from client
            data = self.connection.recv(1024)
            if not data:
                break

            response = client.process(data)
            self.connection.sendall(response.encode('UTF-8'))

        # if break
        self.connection.close()
