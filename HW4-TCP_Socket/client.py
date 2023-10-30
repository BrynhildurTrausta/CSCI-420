'''
	Name: Brynhildur Traustadottir
	Date: 10/29/2023
	Desc: TCP Demo - Client
'''
# Demo for TCP - Multi-threaded so it can print messages from the server
# and allow the user to send

import socket, threading, sys, pickle
from tkinter import *

name = input("Please insert your name: ")

def checkMsg(event=None):
	global sent_count
	msg = input_message.get()
	input_message.delete(0, END)
	sent_count += 1
	message = pickle.dumps({'Name': name, 'msg': msg, 'Count': sent_count})
	s.sendall(message)

master = Tk()

master.geometry("400x300")
master.configure(background="white")
master.title(f"{name}'s TCP chat")

# Create a listbox for displaying messages
message_list = Listbox(master)
message_list.pack(fill=BOTH, expand=True)

# Create an Entry widget for typing messages
input_message = Entry(master) #Text(master, height=1, width = 20)
input_message.pack(fill=X)

# Create a Send button to send messages
#send_button = Button(master, text="Send", command=checkMsg)
#send_button.pack(fill=X)

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
input_message.bind('<Return>', checkMsg)

# sending the name to the server
#send_name = pickle.dumps(name)
#s.sendall(send_name)

while True:
	message = input("What to send? ")
	sent_count += 1
	msg = pickle.dumps({'msg': message, 'Count': sent_count}) # dumps returns the pickle representation object as a bytes object
	s.sendall(msg) 
s.close() # inverse of s.connect()


master.mainloop()

