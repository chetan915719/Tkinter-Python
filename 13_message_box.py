# Import libraries
from tkinter import *
from tkinter import messagebox



# Functions

def info():
	global label

	box = messagebox.showinfo("This is messagebox","Successful")

	label.pack_forget()
	label = Label(__root,text=box,relief=SUNKEN)
	label.pack()

def error():
	global label

	box = messagebox.showerror("This is messagebox","Successful")

	label.pack_forget()
	label = Label(__root,text=box,relief=SUNKEN)
	label.pack()

def warn():
	global label

	box = messagebox.showwarning("This is messagebox","Successful")

	label.pack_forget()
	label = Label(__root,text=box,relief=SUNKEN)
	label.pack()

def askQ():
	global label

	box = messagebox.askquestion("This is messagebox","Successful")

	label.pack_forget()
	label = Label(__root,text=box,relief=SUNKEN)
	label.pack()

def cancel():
	global label

	box = messagebox.askokcancel("This is messagebox","Successful")

	label.pack_forget()
	label = Label(__root,text=box,relief=SUNKEN)
	label.pack()

def yesNo():
	global label

	box = messagebox.askyesno("This is messagebox","Successful")

	label.pack_forget()
	label = Label(__root,text=box,relief=SUNKEN)
	label.pack()

# Root functions

__root = Tk()


# Others


# Create Widgets

button_1 = Button(__root,text="INFO!!!",command=info)
button_2 = Button(__root,text="Error!!!",command=error)
button_3 = Button(__root,text="Warning!!!",command=warn)
button_4 = Button(__root,text="ASK Question!!!",command=askQ)
button_5 = Button(__root,text="Ask cancel !!!",command=cancel)
button_6 = Button(__root,text="Ask yes no !!!",command=yesNo)

label = Label(__root,text="ANS",relief=SUNKEN)


# Add Widgets

button_1.pack(padx=10,pady=10)
button_2.pack(padx=10,pady=10)
button_3.pack(padx=10,pady=10)
button_4.pack(padx=10,pady=10)
button_5.pack(padx=10,pady=10)
button_6.pack(padx=10,pady=10)

label.pack()

# Main Loop

__root.mainloop()