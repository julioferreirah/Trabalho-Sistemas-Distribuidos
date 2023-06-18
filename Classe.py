import xmlrpc.client
import socket

class Mensagem:
    def __init__(self):
        self.destinatario = ""
        self.txt = ""
        self.status = 0

    def to_xmlrpc(self):
        return {
            'string': xmlrpc.client.Binary(self.destinatario.encode('utf-8')),
            'string1': xmlrpc.client.Binary(self.txt.encode('utf-8')),
            'int': self.status
        }

    def from_xmlrpc(self, data):
        self.destinatario = data['string'].data.decode('utf-8')
        self.txt = data['string'].data.decode('utf-8')
        self.status = data['int']

    def function(self):
        self.txt = 'txt'
        self.destinatario = socket.gethostname
        self.status = 1
        return self
