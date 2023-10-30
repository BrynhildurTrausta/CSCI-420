'''
	Name: Brynhildur Traustadottir
	Date: 10/29/2023
	Desc: TCP Demo - Client
			- Multi-threaded that allowes the user to send messages to other users	
				and print messages from the server
			- Client sends message through GUI
			- User sets their name and it displays to everyone
'''

import socket, threading, sys, pickle
from tkinter import *

name = input("Please insert your name: ")

# Function sends message from GUI to all clients
def send_msg(event=None):
	global sent_count
	msg = new_msg.get()
	new_msg.delete(0, END)
	sent_count += 1
	message = pickle.dumps({'Name': name, 'Message': msg, 'Count': sent_count})
	s.sendall(message)

# Makes the GUI
master = Tk()
master.geometry("400x300")
master.configure(background="white")
master.title(f"{name}'s TCP chat")

box = Listbox(master) # For displaying messages
box.pack(fill=BOTH, expand=True)
new_msg = Entry(master) # For typing messages
new_msg.pack(fill=X)

server_ip = "127.0.0.1"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function for receiving messages
def listenThread():
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

# starts send_msg function when pressed enter in GUI
new_msg.bind('<Return>', send_msg)


while True:
	message = input("What to send? ")
#	sent_count += 1
#	msg = pickle.dumps({'msg': message, 'Count': sent_count}) # dumps returns the pickle representation object as a bytes object
#	s.sendall(msg) 


s.close() # Closes the connection to the server, inverse of s.connect()


master.mainloop() # Starts the GUI

