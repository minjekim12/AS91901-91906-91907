"""
Author: Minje Kim
Date Created: June 27, 2023
Description: SpellCraft is an interactive literacy quiz program that allows learners
             to be engaged and encouraged to test and develop their English vocabulary
             and spelling skills. 
"""

# ------------------------------- TKINTER WINDOW PROPERTIES ---------------------------------- #

# Imports everything from Tkinter - Python standard GUI library
from tkinter import * 

# Imports Python Imaging Library(PIL) - ImageTk and Image in order to display background images. 
from PIL import ImageTk, Image  

# Creates root widget - Main window for GUI
root = Tk() 
root.title("SpellCraft")

# Main window properties
window_width = 960
window_height = 540

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



# --------------------------------- BACKGROUND IMAGES PROPERTIES ----------------------------------

# Main Menu Background Image
mainmenu_open = Image.open('resources/main_menu_bg.png') # Opens Image
mainmenu_bg = ImageTk.PhotoImage(mainmenu_open) # Assign into a ImageTk.Photoimage widget. 

# Tutorial Page Background Image
tutorial_open = Image.open('resources/tutorial_bg.png') # Opens Image
tutorial_bg = ImageTk.PhotoImage(tutorial_open) # Assign into a ImageTk.Photoimage widget.

# --------------------------------- MAIN MENU ------------------------------------

# Display Main Menu Background Image
main_menu_bg_label = Label(root, image=mainmenu_bg)
main_menu_bg_label.place(x = 0,y = 0)

# Add text
game_description_label = Label(root, text = "FILL IN THE LETTERS TO MAKE AS MANY \n WORDS AS YOU CAN!!",
               font=("DIN Alternate", 24), fg=("#1b3652"), padx=15, pady=3)
game_description_label.place(x=240, y=340)

tutorial_button = Button(root, text="TUTORIAL", font=("DIN Alternate", 24), fg=("#1b3652"), bg=("white"), padx=7, pady=9, borderwidth=0) #command=TUTORIALPAGE)
tutorial_button.place(x=240, y=420)

game_start_button = Button(root, text="PLAY", font=("DIN Alternate", 24), fg=("#1b3652"), bg=("white"), padx=29, pady=9, borderwidth=0)
game_start_button.place(x=397, y=420)

settings_button = Button(root, text="SETTINGS", font=("DIN Alternate", 24), fg=("#1b3652"), bg=("white"), padx=7, pady=9, borderwidth=0)
settings_button.place(x=555, y=420)





# ------------------ EXECUTE PYTHON ------------------------
# Runs the program and loops to keep it open until closed
root.mainloop() 