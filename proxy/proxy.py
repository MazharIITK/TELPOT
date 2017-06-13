#!/usr/bin/env python

from socket import *

LISTEN_PORT = 9620
SERVER_PORT = 8000 
SERVER_ADDR = gethostbyname("server")
 
from twisted.internet import protocol, reactor, endpoints


class ServerProtocol(protocol.Protocol):
    def __init__(self):
        self.buffer = None
        self.client = None
 
    def connectionMade(self):
    	fd = open("/proxy/log_directory/logs.dat", "a+")
    	mape = '{}\n'.format(self.transport.getPeer())
    	fd.write(mape)
        print 'Connection made to', self.transport.getHost()
        print 'from', self.transport.getPeer()
        factory = protocol.ClientFactory()
        factory.protocol = ClientProtocol # setting the clientProtocol
        factory.server = self
        reactor.connectTCP(SERVER_ADDR, SERVER_PORT, factory)
 
    # Client => Proxy
    def dataReceived(self, data):
        if self.client:
            self.client.write(data)
        else:
            self.buffer = data
 
    # Proxy => Client
    def write(self, data):
        self.transport.write(data)
 

#As client 
class ClientProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.server.client = self
        self.write(self.factory.server.buffer)
        self.factory.server.buffer = ''
 
    # Server => Proxy
    def dataReceived(self, data):
        self.factory.server.write(data)
 
    # Proxy => Server
    def write(self, data):
        if data:
            self.transport.write(data)
 
 
 
def main():
    factory = protocol.ServerFactory()
    factory.protocol = ServerProtocol
 
    reactor.listenTCP(LISTEN_PORT, factory)
    reactor.run()
 
 
if __name__ == '__main__':
    main()
