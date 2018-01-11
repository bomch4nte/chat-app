# -*- coding: cp1254 -*-
#
#

import socket
import util

class Server:
    def __init__(self, host ='0.0.0.0', port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host,port))
    def main(self):
        self.cli, addr = self.s.accept()
        while True:
            message = raw_input("Mesajinizi Giriniz : ")
            util.send(self.cli, message)
            print(util.recv(self.cli))
            
if __name__ == '__main__':
    server = Server(port=8000)
    server.main()
