# Demo for TCP - Multi-threaded so it can print messages from the server
# and allow the user to send

import socket, threading, sys

server_ip = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listenThread():
	global s 
	while True:
		msg = s.recv(1024)
		if len(msg) == 0:
			msg = msg.decode('UTF-8')
			print(msg)

s.connect( (server_ip, port) ) # creating a tcp connection
print("server connected")
thread = threading.Thread(target = listenThread).start()
while True:
	message = input("What to send? ")
	s.sendall(message.encode('ASCII')) # same as utf-8, except utf handles unicode
s.close() # inverse of s.connect()
