#import libraries

from tkinter import *


#functions

def onClick():
	label = Label(root,text=inputBox.get())
	label.pack()


#create widgets

root = Tk()

inputBox = Entry(root,width=50,borderwidth=5)
button = Button(root,text="Click Me!!",command=onClick)

#add widgets

inputBox.pack()
button.pack()

#main loop

root.mainloop()