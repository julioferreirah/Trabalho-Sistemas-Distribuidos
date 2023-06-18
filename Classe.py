import xmlrpc.client

class Class:
    def __init__(self):
        self.string = ''
        self.int = 0

    def to_xmlrpc(self):
        return {
            'string': xmlrpc.client.Binary(self.string.encode('utf-8')),
            'int': self.int
        }

    def from_xmlrpc(self, data):
        self.string = data['string'].data.decode('utf-8')
        self.int = data['int']

    def function(self):
        self.string = 'string'
        self.int = 1
        return self
