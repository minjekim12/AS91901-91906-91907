"""
Author: Minje Kim
Date Created: June 27, 2023
Description: SpellCraft is an interactive literacy quiz program that allows learners
             to be engaged and encouraged to test and develop their English vocabulary
             and spelling skills. 
"""

# imports everything from Tkinter - Python standard GUI library
from tkinter import * 

# Creates root widget - Main window for GUI
root = Tk() 
root.title("SpellCraft")

# Main window properties
window_width = 1000
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# block users from resizing the window - this specific program needs to be at a fixed proportion of display. 
root.resizable(False, False)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Runs the program and loops to keep it open until closed
root.mainloop() 