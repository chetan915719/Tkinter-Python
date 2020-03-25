#import libraries

from tkinter import *


# Functions

def onClick_num(number):
	num = box.get()
	box.delete(0,END)
	box.insert(0,str(num)+str(number))

def onClick_clear():
	box.delete(0,END)

def onClick_op(op):
	global first_num
	global operation

	first_num = float(box.get())
	operation = op
	box.delete(0,END)

def onClick_eq():
	global second_num
	second_num = float(box.get())
	box.delete(0,END)

	if operation == "+":
		result = first_num + second_num
	if operation == "-":
		result = first_num - second_num
	if operation == "/":
		if second_num == 0:
			box.insert(0,"ZERO error")
			return
		else:
			result = first_num / second_num
	if operation == "*":
		result = first_num * second_num

	box.insert(0,result)



# Create root

root = Tk()


# Properties of root

root.title("Simple Calculator")



#create widgets

box = Entry(root,width=35,borderwidth=5)

button_1 = Button(root,text="1",padx=40,pady=20,command= lambda: onClick_num(1))
button_2 = Button(root,text="2",padx=40,pady=20,command= lambda: onClick_num(2))
button_3 = Button(root,text="3",padx=40,pady=20,command= lambda: onClick_num(3))
button_4 = Button(root,text="4",padx=40,pady=20,command= lambda: onClick_num(4))
button_5 = Button(root,text="5",padx=40,pady=20,command= lambda: onClick_num(5))
button_6 = Button(root,text="6",padx=40,pady=20,command= lambda: onClick_num(6))
button_7 = Button(root,text="7",padx=40,pady=20,command= lambda: onClick_num(7))
button_8 = Button(root,text="8",padx=40,pady=20,command= lambda: onClick_num(8))
button_9 = Button(root,text="9",padx=40,pady=20,command= lambda: onClick_num(9))
button_0 = Button(root,text="0",padx=40,pady=20,command= lambda: onClick_num(0))
button_d = Button(root,text=".",padx=42,pady=20,command= lambda: onClick_num("."))
button_00 = Button(root,text="00",padx=37,pady=20,command= lambda: onClick_num("00"))

button_c = Button(root,text="C",padx=40,pady=10,command=onClick_clear)
button_di = Button(root,text="/",padx=40,pady=10,command=lambda: onClick_op("/"))
button_m = Button(root,text="*",padx=40,pady=10,command=lambda: onClick_op("*"))

button_s = Button(root,text="-",padx=20,pady=10,command=lambda: onClick_op("-"))
button_a = Button(root,text="+",padx=20,pady=52,command=lambda: onClick_op("+"))
button_e = Button(root,text="=",padx=20,pady=52,command=onClick_eq)

#add widgets

box.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

button_c.grid(row=1,column=0)
button_di.grid(row=1,column=1)
button_m.grid(row=1,column=2)
button_s.grid(row=1,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_a.grid(row=2,column=3,rowspan=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_e.grid(row=4,column=3,rowspan=2)

button_00.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_d.grid(row=5,column=2)


#main loop

root.mainloop()