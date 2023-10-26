# Demo for TCP - Multi-threaded so it can print messages from the server
# and allow the user to send

import socket, threading, sys, pickle

server_ip = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listenThread(): # we have this function so we can be contantly receiving messages
	global s 
	while True:
		msg = s.recv(1024)
		if len(msg) == 0:
			sys.exit(1)
		decoded = pickle.loads(msg)
		print(decoded)

s.connect( (server_ip, port) ) # creating a tcp connection
print("server connected")
thread = threading.Thread(target = listenThread).start()
sent_count = 0
while True:
	message = input("What to send? ")
	sent_count += 1
	msg = pickle.dumps({'msg': message, 'Count': sent_count}) # dumps returns the pickle representation object as a bytes object
	s.sendall(msg) 
s.close() # inverse of s.connect()
