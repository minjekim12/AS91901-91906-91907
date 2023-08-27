import tkinter as tk
from PIL import ImageTk, Image

def open_toplevel():
    options_window = tk.Toplevel(root)
    options_window.title("Options")
    options_window.geometry("500x380")
    options_window['bg']="#024762"

    def yes_button_click(event):
        print("Button clicked")
        root.destroy()

    def no_button_click(event):
        print("noButton clicked")
        options_window.destroy()
    
    options_window.grab_set()  # Prevent interactions with the main window

    # Load and display the image using ImageTk.PhotoImage
    quit_game_image = Image.open("resources/quit_game_new.png")
    quit_game_photoimage = ImageTk.PhotoImage(quit_game_image)
    
    quit_game_label = tk.Label(options_window, image=quit_game_photoimage, bg="#024762")
    quit_game_label.place(x=80, y=50)
    
    # Keep a reference to the PhotoImage object to prevent it from being garbage collected
    quit_game_label.photo = quit_game_photoimage


    # Load the image for the button
    yes_button_image = Image.open("resources/yes_button.png")
    yes_photoimage = ImageTk.PhotoImage(yes_button_image)

    # Create a label with the image as its content
    yes_button_label = tk.Label(options_window, image=yes_photoimage, bg="#024762")
    yes_button_label.place(x=50, y=200)

    # Keep a reference to the PhotoImage object
    yes_button_label.photo = yes_photoimage

    # Bind the button click function to the label's click event
    yes_button_label.bind("<Button-1>", yes_button_click)


    # Load the image for the button
    no_button_image = Image.open("resources/no_button.png")
    no_photoimage = ImageTk.PhotoImage(no_button_image)

    # Create a label with the image as its content
    no_button_label = tk.Label(options_window, image=no_photoimage, bg="#024762")
    no_button_label.place(x=260, y=205)

    # Keep a reference to the PhotoImage object
    no_button_label.photo = no_photoimage

    # Bind the button click function to the label's click event
    no_button_label.bind("<Button-1>", no_button_click)

    

    

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

# Main Window Properties
root = tk.Tk()
root.title("SpellCraft")

window_width = 960
window_height = 540

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.resizable(False, False)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

mainmenu_open = Image.open("resources/main_menu_bg.png")
mainmenu_bg = ImageTk.PhotoImage(mainmenu_open)
main_menu_bg_label = tk.Label(root, image=mainmenu_bg)

tutorial_open = Image.open("resources/tutorial_bg.png")
tutorial_bg = ImageTk.PhotoImage(tutorial_open)
tutorial_bg_label = tk.Label(root, image=tutorial_bg)

main_menu_bg_label.place(x=0, y=0)

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

open_new_window_button = tk.Button(
    root,
    text="X",
    font=("DIN Alternate", 20),
    bg="blue",
    padx=7,
    pady=5,
    borderwidth=0,
    highlightbackground="#98eaf4",
    command=open_toplevel,
)
open_new_window_button.place(x=20, y=20)

root.mainloop()
