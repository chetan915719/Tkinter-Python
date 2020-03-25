# Import libraries
from tkinter import *



# Functions



# Root functions

__root = Tk()


# Others



# Create Widgets
__frame = LabelFrame(__root,text="This is frame...",padx=50,pady=50)
__button = Button(__frame,text="Click Me!!!")


# Add Widgets
__frame.pack(padx=10,pady=10)
__button.pack()


# Main Loop

__root.mainloop()