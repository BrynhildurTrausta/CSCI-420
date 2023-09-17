'''
	Name: Brynhildur Traustadottir
	Date: 09/17/23
	Desc: Press the mouse as fast as you can as it moves every 2 seconds.
'''

from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
import time


master = Tk()

# Making th background look like an image, convert to GIF
mouse_hs = Image.open("mouse_house.png")
size2 = (800, 600)
bckgr = mouse_hs.resize(size2)
bckgr.save("mouse_house.gif", "GIF")

bgimg = PhotoImage(file = "mouse_house.gif")
limg= Label(master, i=bgimg)
limg.pack()

master.geometry("800x600")
#master.configure(background="white")
i = 0
j = 0
clk_time = 0 
avg = 0
react_dict = {}
a = 0

# Funtion to make the button move randomly
def moving(enter = None):
	global i, j, clk_time
	i = random.randrange(0, 367)
	j = random.randrange(0, 367)
	btn.place(x = i, y = j)
	btn.after(2000, moving)
	clk_time = time.time()

# Function for the reaction time of the button
def buttonClicked(event = None):
	global clk_time, a
	elapsed = time.time() - clk_time
	#print(f"Reaction Time: {elapsed:0.2f}")
	react_dict[a] = elapsed
	a += 1


# Making the button look like an image, have to have the image in a GIF format
image = Image.open("mouse.png")
size = (50, 50)
new_image = image.resize(size)
new_image.save("mouse.gif", "GIF")
image = PhotoImage(file="mouse.gif")

btn = Button(master, image = image, text = "")
btn.after(2, moving)
btn.bind('<Button>', buttonClicked)


mainloop()

# Printing out the reaction time & avg time
y = 0
for x in react_dict.keys():
	y += react_dict[x]
	print(f"{x + 1}: {react_dict[x]:0.2f}", end = '')
	print()

reac_time = y/a
print(f"Average Reaction Time: {reac_time:0.2f}")
print()