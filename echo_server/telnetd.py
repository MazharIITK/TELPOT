#!/usr/bin/python

from socket import *
from threading import Thread

s = socket()
host = gethostname()

server_port = 8000

s.bind((host, server_port))

print host

s.listen(2)

while True:
	dup_sd, addr = s.accept()
    
	print("New client connected")
	while True:
    		message = dup_sd.recv(1024)
    		if len(message) == 0:
    			print("Client disconnected")
    			break
    		print 'Message from client: %s\n' % (message)
    	
    		dup_sd.send(message)
	dup_sd.close()
