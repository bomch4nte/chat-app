# -*- coding: utf-8 -*-
#
#

import socket
import util

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
    def main(self):
        self.s.connect((self.host, self.port))
        while True:
            print(util.recv(self.s))
            message = raw_input("Cevap ver : ")
            util.send(self.s, message)

if __name__ == '__main__':
    client = Client(host='127.0.0.1', 8000)
    client.main()
    
