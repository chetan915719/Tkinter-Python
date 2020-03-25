from tkinter import *
from PIL import ImageTk, Image

# Fuctions


# Root properties

root = Tk()
root.title("Image")
root.iconbitmap("icon.ico")


# Others

img = ImageTk.PhotoImage(Image.open("images/img.png"))

# Widgets

label = Label(image=img)
exit = Button(root,text="Exit",command=root.quit)


# Add Widgets

label.pack()
exit.pack()


# Main Loop

root.mainloop()