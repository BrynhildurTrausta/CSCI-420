'''
	Name: Brynhildur Traustadottir
	Date: 09/27/23
	Desc: Terminal UDP Chat System - The client
'''
import socket
import threading
import time

port = 5555 # anything over 1024. 
ip_server = "127.0.0.1" # Me. The machine you plan on communicating with

sock_ready = False
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def listenThread():
	global s
	global sock_ready
	while not sock_ready:
		time.sleep(0.1)
	while True:
		(msg, addr) = s.recvfrom(1024)
		msg = msg.decode('UTF-8')
		print(msg)

thread = threading.Thread(target=listenThread).start()

while True:
	message = input("Enter a message: ")

	s.sendto(message.encode('UTF-8'), (ip_server, port) ) #Send it to that up adress and porter
	sock_ready = True
