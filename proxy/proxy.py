#!/usr/bin/env python

import datetime
import os
from socket import *

LISTEN_PORT = 23
SERVER_PORT = 8000 
SERVER_ADDR = gethostbyname("server")
 
from twisted.internet import protocol, reactor, endpoints

class ServerProtocol(protocol.Protocol):
    def __init__(self):
        self.buffer = None
        self.client = None
    
    def connectionMade(self, trigger=0):
    	if(trigger==0):
    		self.checker = 0
    		self.attempts = 3
    		self.transport.write("Login authentication\n\n")
    		self.transport.write("Login username: ")
    		attack_ip, attack_port = self.transport.client
    		print attack_ip
    		print attack_port
   
    		path = "/proxy/log_directory/"+attack_ip
    	
    		if os.path.exists(path) == False and trigger==0:
    			os.makedirs(path)
    		
    			time = (datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    		
    			completeName = os.path.join(path, time+".dat")
    		
			self.fd = open(completeName, "a+")
			IPandPORT = attack_ip + ':' + str(attack_port) + '\n'
			self.fd.write(IPandPORT)
		else:
			time = (datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    		
    			completeName = os.path.join(path, time+".dat")
    		
			self.fd = open(completeName, "a+")
			data = attack_ip + ':' + str(attack_port) + '\n'
			self.fd.write(data)		 
        	factory = protocol.ClientFactory()
        	factory.protocol = ClientProtocol
        	factory.server = self
        	reactor.connectTCP(SERVER_ADDR, SERVER_PORT, factory)
	
	
	elif(trigger==1):
		return self.fd
 
    # Client to Proxy
    def dataReceived(self, data):
        if self.client:
            self.client.write(data)
            new_fd = self.connectionMade(1)
            new_fd.write(data)
            new_fd.flush()
            os.fsync(new_fd)
        else:
            self.buffer = data

    # Proxy to Client
    def write(self, data):
    	if self.checker==0:
    		self.transport.write("Login password: ")
    		self.checker = 1
    		self.attempts = self.attempts-1
    	elif self.checker==1:
    		just = str(self.attempts)
    		self.transport.write("Login Invalid\nTry Again!!: \n")
    		self.transport.write(just)
    		self.transport.write(" trials left\n")
    		self.transport.write("Login password: ")
    		self.checker = 2
    		self.attempts = self.attempts-1
    	elif self.checker==2:
    		just = str(self.attempts)
    		self.transport.write("Login Invalid\nTry Again!!: \n")
    		self.transport.write(just)
    		self.transport.write(" trials left\n")
    		self.transport.write("Login password: ")
    		self.checker = 3
    		self.attempts = self.attempts-1
    	elif self.checker==3:
    		just = str(self.attempts)
    		self.transport.write("Login Invalid\nTry Again!!: \n")
    		self.transport.write(just)
    		self.transport.write(" trials left\n")
    		self.checker = 4
        else:
    		self.transport.write("Sorry, this will not work now\n")
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
