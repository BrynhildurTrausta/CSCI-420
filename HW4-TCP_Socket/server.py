# Demo for TCP - Server
# Can handle multiple clients at a time due to threading

import socket, threading


port = 5555

def TCPWorker(sockets, client_socket):
	print("Got accept, waiting for packet")
	while True:
		try:
			
			msg = client_socket.recv(1024)
			if len(msg) == 0:
				break # after this loop it starts waiting for more clients
			print(msg.decode("ASCII"))
			client_socket.sendall("OK".encode("ASCII"))
			for c in sockets:
				if c != client_socket:
					c.sendall(msg)
		except Exception as e:
			print(f"Got {e}")
			break
	sockets.remove(client_socket)
	print("TCP Worker died")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	sockets = []
	s.bind( ('0.0.0.0', port) ) # tells the server to start listening on all the devices on this server
	s.listen(0)
	print("Server waiting")
	while True:
		print("waiting for accept")
		client_socket, addr = s.accept() # accepted a new client connection. Here we have two sockets. 
											# s is client socket it accepts new connections, 
											# other is client_socket. the connection to the client
		print(f"Got accept from {addr}")
		sockets.append(client_socket)
		threading.Thread(target=TCPWorker, args = [sockets, client_socket]).start()
	s.close() # inverse of s.connect()