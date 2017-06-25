#!/usr/bin/env python

import time
import datetime
import os
import sys
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
    		self.ban = open("/proxy/banner.dat", "rb")
    		self.l = self.ban.read(1024)
    		while (self.l):
    			self.transport.write(self.l)
            		self.l = self.ban.read(1024)
        	self.ban.close()
    		self.transport.write("\n\nLogin authentication\n\n")
    		self.transport.write("Login username: ")
    		attack_ip, attack_port = self.transport.client
    		print attack_ip
    		print attack_port
   
    		path = "/proxy/log_directory/"+attack_ip
    		
    		path_IP_PORT = "/proxy/IP_PORT/"
    		self.path_UNAME_PASS = "/proxy/UNAME_PASS/"
    		
    		if os.path.exists(path) == False and trigger==0:
    			os.makedirs(path)
    		
    			time = (datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    			
    			time2 = (datetime.datetime.today().strftime('%Y-%m-%d'))
    			
    			completeName = os.path.join(path, time+".dat")
    			
    			path_IP_PORT_file_name = os.path.join(path_IP_PORT, time2+".dat")
    			
    			path_UNAME_PASS_file_name = os.path.join(self.path_UNAME_PASS, time2+".dat")
    			
			self.fd = open(completeName, "a+")
			IPandPORT = attack_ip + ':' + str(attack_port) + '\n'
			self.fd.write(IPandPORT)
			
			self.IP_PORT_fd = open(path_IP_PORT_file_name, "a+")
			IPandPORT = attack_ip + ',' + str(attack_port) + '\n'
			self.IP_PORT_fd.write(IPandPORT)
			
		else:
			time = (datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
			
			time2 = (datetime.datetime.today().strftime('%Y-%m-%d'))
    		
    			completeName = os.path.join(path, time+".dat")
    			
    			path_IP_PORT_file_name = os.path.join(path_IP_PORT, time2+".dat")
    			
    			self.path_UNAME_PASS_file_name = os.path.join(self.path_UNAME_PASS, time2+".dat")
    			
			self.fd = open(completeName, "a+")
			data = attack_ip + ':' + str(attack_port) + '\n'
			self.fd.write(data)
			
			self.IP_PORT_fd = open(path_IP_PORT_file_name, "a+")
			IPandPORT = attack_ip + ',' + str(attack_port) + '\n'
			self.IP_PORT_fd.write(IPandPORT)
			self.IP_PORT_fd.flush()   
            		os.fsync(self.IP_PORT_fd)
					
					 
        	factory = protocol.ClientFactory()
        	factory.protocol = ClientProtocol # setting the clientProtocol
        	factory.server = self
        	reactor.connectTCP(SERVER_ADDR, SERVER_PORT, factory)
	
	
	elif(trigger==1):
		return self.fd
	
	elif(trigger==2):
		time2 = (datetime.datetime.today().strftime('%Y-%m-%d'))
		path_UNAME_PASS_file_name = os.path.join(self.path_UNAME_PASS, time2+".dat")
		self.UNAME_PASS_fd = open(self.path_UNAME_PASS_file_name, "a+")
		return self.UNAME_PASS_fd
		
 
    # Client => Proxy
    def dataReceived(self, data):
        if self.client:
            self.client.write(data)
            new_fd = self.connectionMade(1)
            new_fd.write(data)
            new_fd.flush()   
            os.fsync(new_fd)
		
	    new_UNAME_PASS_fd = self.connectionMade(2)
            new_UNAME_PASS_fd.write(data)
            new_UNAME_PASS_fd.flush()   
            os.fsync(new_UNAME_PASS_fd)
            
        else:
            self.buffer = data

    # Proxy => Client
    def write(self, data):
    	if self.checker==0:
    		self.transport.write("\nLogin password: ")
    		self.checker = 1
    	elif self.checker==1:
            	time.sleep(2)
    		self.transport.write("\nslight mispelling. Please check the password and Try Again!!\n")
            	time.sleep(2)
            	self.transport.write("\nLogin username: ")
    		self.checker = 2.1
    	elif self.checker==2.1:
    		self.transport.write("\nLogin password: ")
    		self.checker = 2.2
    	elif self.checker==2.2:
            	time.sleep(2)
            	self.transport.write("\nLogin Invalid\nTry Again!!: \n")
            	self.transport.write("Login username: ")
    		self.checker = 2
    	elif self.checker==2:
    		self.transport.write("\nLogin password: ")
    		self.checker = 3
    	elif self.checker==3:
            	time.sleep(2)
    		self.transport.write("\nSomething went wrong !!\nPlease press ENTER.\nCheck the caps-lock key and retype the password.\n")
    		time.sleep(2)
            	self.checker = 3.1
        elif self.checker==3.1:
            	self.transport.write("\nLogin username: ")
    		self.checker = 0
    		 

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
