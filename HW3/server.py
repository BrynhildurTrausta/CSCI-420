'''
	Name: Brynhildur Traustadottir
	Date: 09/27/23
	Desc: Terminal UDP Chat System - The Server
'''

import socket

listen_port = 5555 # anything over 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('0.0.0.0', listen_port) )

clients = set()

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)
	clients.add(addr)
	print(clients)

	msg = msg.decode('UTF-8')
	print(f"{addr}: {msg}")

	msg = f'{addr}: {msg.lower()}'

	for c in clients:
		s.sendto(msg.encode('UTF-8'), c )

