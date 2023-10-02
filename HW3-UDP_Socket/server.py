'''
	Name: Brynhildur Traustadottir
	Date: 09/27/23
	Desc: Terminal UDP Chat System - The Server
'''

import socket
from datetime import datetime

listen_port = 5555 # anything over 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('0.0.0.0', listen_port) )

clients = {}

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)
	msg = msg.decode('UTF-8')

	if msg.startswith('/Name '):
		Name = msg.split(" ", 1)[1]
		clients[addr] = clients.get(addr, f'{Name}')
		print(clients)
		continue

	clients[addr] = clients.get(addr, f'{Name}')
	print(clients)

	now = datetime.now()
	currentTime = now.strftime("%H:%M:%S")

	print(f"At {currentTime} {addr} said: {msg}")

	msg = f'{addr}: {msg.lower()}'

	for c in clients:
		s.sendto(msg.encode('UTF-8'), c )

