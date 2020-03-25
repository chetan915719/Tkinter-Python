from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Fuctions
def onClick():
	root.filename = filedialog.askopenfilename(initialdir='',title='Select  a file',filetypes=(("png files","*.png"),("all files","*.*")))

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