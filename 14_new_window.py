from tkinter import *
from PIL import ImageTk, Image

# Fuctions
def onClick():
	top = Toplevel()
	top.title("Second Window")
	top.iconbitmap("icon.ico")

	img = ImageTk.PhotoImage(Image.open("images/img.png"))
	label = Label(top,image=img).pack()

# Root properties

root = Tk()
root.title("Image")
root.iconbitmap("icon.ico")


# Others



# Widgets

button = Button(root,text="Click Me!!!",command=onClick)


# Add Widgets

button.pack()


# Main Loop

root.mainloop()