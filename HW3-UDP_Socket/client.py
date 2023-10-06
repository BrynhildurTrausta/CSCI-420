'''
	Name: Brynhildur Traustadottir
	Date: 09/27/23
	Desc: Terminal UDP Chat System - The client
		  Include the time that each message was sent to all users
		  Allow the user to set their name to an address
'''
import socket
import threading
import time

port = 5555 # anything over 1024. 
ip_server = "127.0.0.1" # Me. The machine you plan on communicating with

sock_ready = False
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# The function that receives the messages from everyone
# that is sent to the server
def listenThread():
	global s, sock_ready
	while not sock_ready:
		time.sleep(0.1)
	while True:
		(msg, addr) = s.recvfrom(1024)
		msg = msg.decode('UTF-8')

		# Getting all options of the special messages
		if msg.startswith("/options"):
			option = input("Pick an option:\n1: Get the number of clients\n2: Get the name of all clients\n3: Send a private message to a specific client\n")
			if "1" in option:
				msg = "numusers?"
			elif "2" in option:
				msg = "users?"
			elif "3" in option:
				name = input("Enter the name of the receiver: ")
				message = input("Ender the desired message: ")
				msg = f"{message}->{name}"
			else:
				pass
			s.sendto(msg.encode('UTF-8'), (ip_server, port) )
			continue
		print(msg)

# Asks the client for its name
def setName():
	global sock_ready
	name = input("Please enter your name: ")
	sock_ready = True
	return name

# The thread to allow messages to be displayed to clients 
# sent by others
thread = threading.Thread(target=listenThread).start()

username = setName()

# Sends the name to the server
s.sendto(f"/Name {username}".encode('UTF-8'), (ip_server, port) ) 

while True:
	message = input("Enter a message: ")

	s.sendto(message.encode('UTF-8'), (ip_server, port) ) #Send it to that up adress and porter
	sock_ready = True
