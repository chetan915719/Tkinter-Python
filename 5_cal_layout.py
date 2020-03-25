#import libraries

from tkinter import *


#functions



#create widgets

root = Tk()

button_1 = Button(root,text="1")
button_2 = Button(root,text="2")
button_3 = Button(root,text="3")
button_4 = Button(root,text="4")
button_5 = Button(root,text="5")
button_6 = Button(root,text="6")
button_7 = Button(root,text="7")
button_8 = Button(root,text="8")
button_9 = Button(root,text="9")
button_0 = Button(root,text="0")
button_d = Button(root,text=".")
button_00 = Button(root,text="00")

#add widgets
button_7.grid(row=0,column=0)
button_8.grid(row=0,column=1)
button_9.grid(row=0,column=2)
button_4.grid(row=1,column=0)
button_5.grid(row=1,column=1)
button_6.grid(row=1,column=2)
button_1.grid(row=2,column=0)
button_2.grid(row=2,column=1)
button_3.grid(row=2,column=2)
button_00.grid(row=3,column=0)
button_0.grid(row=3,column=1)
button_d.grid(row=3,column=2)


#main loop

root.mainloop()