import socket
import pickle

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.103"
        self.port = 5555
        self.address = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048*8))
        except socket.error as e:
            raise e

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*8))
        except socket.error as e:
            print(e)
        except EOFError:
            return KeyError

    #def get_id(self, name):
    #    try:
    #        self.client.send(str.encode("get_id " + name))
    #        return self.client.recv(2048).decode("ISO-8859-1")
    #    except socket.error as e:
    #        print(e)
