#import libraries

from tkinter import *


#create widgets

root = Tk()

label1 = Label(root,text="Hello World !!!!")
label2 = Label(root,text="Welcome to Python GUI")

#add widgets
label1.grid(row=0,column=0)
label2.grid(row=1,column=1)


#main loop

root.mainloop()