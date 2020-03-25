from tkinter import *
from PIL import ImageTk, Image

# Global Variable

global current_position

# Fuctions

def forward():
	global current_position
	global label
	global nextImg
	global status


	if current_position > len(imgLst)-2:
		nextImg = Button(root,text=">>",state=DISABLED)
	else:
		current_position += 1
		label.grid_forget()
		label = Label(image=imgLst[current_position])
		label.grid(row=0,column=0,columnspan=3)

		status.grid_forget()
		status = Label(root,text="Image : "+str(current_position+1)+" of "+str(len(imgLst)),bd=1,bg="#dedede",anchor=E,relief=SUNKEN)
		status.grid(row=2,column=0,columnspan=3,sticky=E+W)



def backward():
	global current_position
	global label
	global preImg
	global status


	if current_position == 0:
		preImg = Button(root,text="<<",state=DISABLED)
	else:
		current_position -= 1
		label.grid_forget()
		label = Label(image=imgLst[current_position])
		label.grid(row=0,column=0,columnspan=3)

		status.grid_forget()
		status = Label(root,text="Image : "+str(current_position+1)+" of "+str(len(imgLst)),bd=1,bg="#dedede",anchor=E,relief=SUNKEN)
		status.grid(row=2,column=0,columnspan=3,sticky=E+W)


# Root properties

root = Tk()
root.title("Image")
root.iconbitmap("icon.ico")


# Others

img1 = ImageTk.PhotoImage(Image.open("images/img.png"))
img2 = ImageTk.PhotoImage(Image.open("images/img2.png"))
img3 = ImageTk.PhotoImage(Image.open("images/img3.png"))
img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))
img5 = ImageTk.PhotoImage(Image.open("images/img5.png"))

imgLst = [img1,img2,img3,img4,img5]
current_position = 0

# Widgets

label = Label(image=img1)
exit = Button(root,text="Exit",command=root.quit)
nextImg = Button(root,text=">>",command=forward)
preImg = Button(root,text="<<",command=backward)
status = Label(root,text="Image : "+str(current_position+1)+" of "+str(len(imgLst)),bd=1,bg="#dedede",anchor=E,relief=SUNKEN)

# Add Widgets

label.grid(row=0,column=0,columnspan=3)
exit.grid(row=1,column=1,pady=10)
nextImg.grid(row=1,column=2)
preImg.grid(row=1,column=0)
status.grid(row=2,column=0,columnspan=3,sticky=E+W)


# Main Loop

root.mainloop()