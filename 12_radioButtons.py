# Import libraries
from tkinter import *



# Functions

def OnClick(value):

	global label

	label.pack_forget()
	label = Label(__root,text="Ans : "+str(r.get()))
	label.pack()


# Root functions

__root = Tk()


# Others
r = IntVar()
r.set("0")


# Create Widgets
rdButton_1 = Radiobutton(__root,text="Option 1",variable=r,value=1,command=lambda: OnClick(r.get()))
rdButton_2 = Radiobutton(__root,text="Option 2",variable=r,value=2,command=lambda: OnClick(r.get()))

label = Label(__root,text="Ans : "+str(r.get()))

# Add Widgets
rdButton_1.pack()
rdButton_2.pack()

label.pack()

# Main Loop

__root.mainloop()