
"""
Author: Minje Kim

Date Created: June 27, 2023

Description: SpellCraft is an interactive literacy quiz program
            that allows learners to be engaged and encouraged
            to test and develop their English vocabulary
            and spelling skills.
"""

import tkinter as tk
from PIL import ImageTk, Image


def tutorial_page():
    """When the tutorial button is pressed, destroy all widgets from menu.

    Then change the background to tutorial.
    """
    main_menu_bg_label.destroy()
    game_description_label.destroy()
    tutorial_button.destroy()
    game_start_button.destroy()
    settings_button.destroy()
    tutorial_bg_label.place(x=0, y=0)


# Creates root widget - Main window for GUI
root = tk.Tk()
root.title("SpellCraft")

# Main window properties
window_width = 960
window_height = 540

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Block users from resizing the window.
root.resizable(False, False)

# Set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Main Menu Background Image
mainmenu_open = Image.open("resources/main_menu_bg.png")
mainmenu_bg = ImageTk.PhotoImage(mainmenu_open)
main_menu_bg_label = tk.Label(root, image=mainmenu_bg)

# Tutorial Page Background Image
tutorial_open = Image.open("resources/tutorial_bg.png")
tutorial_bg = ImageTk.PhotoImage(tutorial_open)
tutorial_bg_label = tk.Label(root, image=tutorial_bg)

# Display Main Menu Background Image
main_menu_bg_label.place(x=0, y=0)

# Add text
game_description_label = tk.Label(
    root,
    text="FILL IN THE LETTERS TO MAKE AS MANY \n WORDS AS YOU CAN!!",
    font=("DIN Alternate", 24),
    fg="#1b3652",
    bg="white",
    padx=15,
    pady=3,
)
game_description_label.place(x=240, y=340)

tutorial_button = tk.Button(
    root,
    text="TUTORIAL",
    font=("DIN Alternate", 24),
    fg="#1b3652",
    bg="white",
    padx=7,
    pady=9,
    borderwidth=0,
    command=tutorial_page,
)
tutorial_button.place(x=240, y=420)

game_start_button = tk.Button(
    root,
    text="PLAY",
    font=("DIN Alternate", 24),
    fg="#1b3652",
    bg="white",
    padx=29,
    pady=9,
    borderwidth=0,
)
game_start_button.place(x=397, y=420)

settings_button = tk.Button(
    root,
    text="SETTINGS",
    font=("DIN Alternate", 24),
    fg="#1b3652",
    bg="white",
    padx=7,
    pady=9,
    borderwidth=0,
)
settings_button.place(x=555, y=420)

# Execute the GUI application
root.mainloop()
