#import libraries

from tkinter import *


#functions
def onClick():
	label = Label(root,text="Button clicked !!!!")
	label.pack()


#create widgets

root = Tk()

button = Button(root,text="Click Me!!!",command=onClick)

#add widgets
button.pack()


#main loop

root.mainloop()