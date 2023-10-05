'''
	Name: Brynhildur Traustadottir
	Date: 09/27/23
	Desc: Terminal UDP Chat System - The Server
		  Include the time that each message was sent to all users
		  Allow the user to set their name to an address
'''

import socket
from datetime import datetime

listen_port = 5555 # anything over 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('0.0.0.0', listen_port) )

clients = {}

while True:
	# Getting the message from the client
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)
	msg = msg.decode('UTF-8')

	# If the message starts with /Name, the client had submitted
	# His name as the first message
	# That name will be the value to the key in the dictionary
	# Which is the Ip address and the port number
	if msg.startswith('/Name '):
		#name = msg.split(" ", 1)[1]
		name = msg[6:]
		clients[addr] = name
		print(f"New User: {name}")
		continue

	# Getting the names of all users in the dictionary
	if msg == "Users?":
		msg = ''
		for ad in clients.keys():
			msg += clients[ad] + ", "
		s.sendto(msg.encode('UTF-8'), addr )
		continue

	# Getting the number of users that is in the dictionary
	if msg == "NumUsers?":
		msg = f"Number of users: {len(clients)}"
		s.sendto(msg.encode('UTF-8'), addr )
		continue

	# Getting the correct name that matches the ip address
	sender_name = clients.get(addr, 'Unknown')
	print(clients)

	# Getting the real time in military time
	now = datetime.now()
	currentTime = now.strftime("%H:%M:%S")
	print(f"From {sender_name} at {currentTime}: {msg}")

	msg = f'{msg.lower()}'

	# sending the messages and the name of the sender to all clients
	for c in clients:
		if c == addr:
			continue
		s.sendto(f"From {sender_name} at {currentTime}: {msg}".encode('UTF-8'), c )

