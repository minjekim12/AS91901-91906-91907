"""
Author: Minje Kim

Date Created: June 27, 2023

Description: SpellCraft is an interactive literacy quiz program
            that allows learners to be engaged and encouraged
            to test and develop their English vocabulary
            and spelling skills.
"""

# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image # For background images
import random
import string
from tkinter import messagebox
import pygame # For background music and volume control
import webbrowser


# Define the main application class
class SpellCraftApp:
    
    # Initialize the main application window
    def __init__(self, root): 
        self.root = root
        self.root.title("SpellCraft") # Set the window title


        # Configure window dimensions and position
        self.window_width = 960
        self.window_height = 540
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        # Configure window properties
        self.root.resizable(False, False) # Disable window resizing
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}")

        # Initialise attributes
        self.main_menu()
        self.game_duration = 60
        self.volume = 0.5  # Set an initial volume level 
        self.user_name = ""
        

    def main_menu(self):

         # Load and display the main menu background image
        self.mainmenu_open = Image.open("resources/main_menu_bg.png")
        self.mainmenu_bg = ImageTk.PhotoImage(self.mainmenu_open)
        self.main_menu_bg_label = tk.Label(self.root, image=self.mainmenu_bg)
        self.main_menu_bg_label.place(x=0, y=0)

        # Create a label displaying the game description
        self.game_description_label = tk.Label(
            self.root,
            text="FILL IN THE LETTERS TO MAKE AS MANY \n WORDS AS YOU CAN!!",
            font=("DIN Alternate", 24),
            fg="#1b3652",
            bg="white",
            padx=15,
            pady=3,
        )
        self.game_description_label.place(x=240, y=340)

        # Create a button to access the tutorial page
        self.tutorial_button = tk.Button(
            self.root,
            text="TUTORIAL",
            font=("DIN Alternate", 24),
            fg="#1b3652",
            bg="white",
            padx=7,
            pady=9,
            borderwidth=0,
            command=self.tutorial_page,
        )
        self.tutorial_button.place(x=240, y=420)

        # Create a button to start the game
        self.game_start_button = tk.Button(
            self.root,
            text="PLAY",
            font=("DIN Alternate", 24),
            fg="#1b3652",
            bg="white",
            padx=29,
            pady=9,
            borderwidth=0,
            command=self.start_game,
        )
        self.game_start_button.place(x=397, y=420)

        # Create a button to access the settings page
        self.settings_button = tk.Button(
            self.root,
            text="SETTINGS",
            font=("DIN Alternate", 24),
            fg="#1b3652",
            bg="white",
            padx=7,
            pady=9,
            borderwidth=0,
            command=self.settings_page, 
        )
        self.settings_button.place(x=555, y=420)

        # Create a button to open a new window (used for quitting the game)
        self.open_new_window_button = tk.Button(
            self.root,
            text="X",
            font=("DIN Alternate", 20),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
            command=self.open_toplevel,
        )
        self.open_new_window_button.place(x=20, y=20)

    def tutorial_page(self):

        # Remove elements from the main menu
        self.main_menu_bg_label.destroy()
        self.game_description_label.destroy()
        self.tutorial_button.destroy()
        self.game_start_button.destroy()
        self.settings_button.destroy()

        # Load and display the settings background image
        self.tutorial_open = Image.open("resources/tutorial_bg.png")
        self.tutorial_bg = ImageTk.PhotoImage(self.tutorial_open)
        self.tutorial_bg_label = tk.Label(self.root, image=self.tutorial_bg)
        self.tutorial_bg_label.place(x=0, y=0)


        # Create a button to open a new window (used for exiting tutorials)
        self.open_tutorial_toplevel_button = tk.Button(
            self.root,
            text="X",
            font=("DIN Alternate", 20),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
            command=self.open_tutorial_toplevel,
        )
        self.open_tutorial_toplevel_button.place(x=20, y=20)

    def settings_page(self):

        # Remove elements from the main menu
        self.main_menu_bg_label.destroy()
        self.game_description_label.destroy()
        self.tutorial_button.destroy()
        self.game_start_button.destroy()
        self.settings_button.destroy()

        # Load and display the settings background image
        self.settings_open = Image.open("resources/settings_bg.png")
        self.settings_bg = ImageTk.PhotoImage(self.settings_open)
        self.settings_bg_label = tk.Label(self.root, image=self.settings_bg)
        self.settings_bg_label.place(x=0, y=0)

        # Create a button to open a new window (used for exiting settings)
        self.open_settings_toplevel_button = tk.Button(
            self.root,
            text="X",
            font=("DIN Alternate", 20),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
            command=self.open_settings_toplevel
        )
        self.open_settings_toplevel_button.place(x=20, y=20)

        # Create a button to open a GitHub link
        self.share_button = tk.Button(
            self.root,
            text="OPEN GITHUB LINK",
            font=("DIN Alternate", 16),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
            command=self.open_github_link
        )
        self.share_button.place(x=600, y=388)

        # Create a Tkinter Scale widget for game duration control
        self.duration_scale = tk.Scale(
            self.root,
            from_=20, to=200,  
            orient="horizontal",
            label="          GAME DURATION",
            font=("DIN Alternate", 14),
            sliderlength=20,
            showvalue=1,
            length=170,
            command=self.update_duration,  # This function will be called when the slider is moved
        )
        self.duration_scale.set(60)  # Set an initial duration
        self.duration_scale.place(x=590, y=215)

        # Create a Tkinter Scale widget for volume control
        self.volume_scale = tk.Scale(
            self.root,
            from_=0, to=100,
            orient="horizontal",
            label="            VOLUME",
            font=("DIN Alternate", 14),
            sliderlength=20,
            showvalue=1,
            length=140,
            command=self.update_volume,  
        )
        self.volume_scale.set(100)  # Set the initial volume level
        self.volume_scale.place(x=183, y=395)  

        # Create an entry widget for the user's name input
        self.name_entry = tk.Entry(
            self.root,
            font=("DIN Alternate", 18),
            bg="white",
            fg="black",
            borderwidth=0,
            highlightbackground="white",
            width=12,
        )
        self.name_entry.place(x=155, y=210)

        # Create a button to submit the user's name
        self.submit_name_button = tk.Button(
            self.root,
            text="Submit",
            font=("DIN Alternate", 14),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
            command=self.submit_user_name,
        )
        self.submit_name_button.place(x=280, y=209)
        

        # Update the name_entry with the stored user name (if available)
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.user_name)

    def submit_user_name(self):

        # Get the user's name from the entry widget
        user_name = self.name_entry.get()

        if user_name.isalpha():
            # If the name is valid (contains only alphabets), store it and show a message box
            self.user_name = user_name
            messagebox.showinfo("Name Submitted", f"Your name: {self.user_name}")
        elif user_name == "":
            # If the user leaves the name field empty, set the name to none and show a message box
            self.user_name = user_name
            messagebox.showinfo("Name Removed", f"Player name set to none.")
        else:
            # If the name contains non-alphabets, show an error message box
            messagebox.showerror("Name Invalid", f"Error: Name must only include alphabets.", icon = 'warning')

   
    
    def update_duration(self, value):
        # Update the game's duration based on the value from the Scale
        self.game_duration = int(value)  # Store the new duration in a variable


    def update_volume(self, value):
        # Update the volume based on the value from the Scale widget (0 to 100)
        self.volume = int(value) / 100.0  # Convert to a decimal value between 0 and 1

        # Update the volume of background music
        pygame.mixer.music.set_volume(self.volume)

        


    def start_game(self):

        # Destroy elements from the main menu to prepare for the game interface
        self.main_menu_bg_label.destroy()
        self.game_description_label.destroy()
        self.tutorial_button.destroy()
        self.game_start_button.destroy()
        self.settings_button.destroy()

        # Load and display the game background image
        self.game_bg_open = Image.open("resources/game_bg.png")
        self.game_bg = ImageTk.PhotoImage(self.game_bg_open)
        self.game_bg_label = tk.Label(self.root, image=self.game_bg)
        self.game_bg_label.place(x=0, y=0)

        # Create an instance of the SpellingGame class and start the game
        game = SpellingGame(self.root, self.game_duration)
        self.in_game_page = True
        game.start_game()
        


    def open_toplevel(self):

        # Create a new Toplevel window
        options_window = tk.Toplevel(root)
        options_window.title("Options")
        options_window.geometry("500x380")
        options_window['bg'] = "#024762"

        def yes_button_click(event): 
            # This function is called when the "Yes" button is clicked
            root.destroy() # Close the main window and quit the program

        def no_button_click(event):
            # This function is called when the "No" button is clicked
            options_window.destroy() # Close the options window

        options_window.grab_set()  # Prevent interactions with the main window while the options window is open

        # Load and display an image for quitting the program
        quit_program_image = Image.open("resources/quit_program?.png")
        quit_program_photoimage = ImageTk.PhotoImage(quit_program_image)
        quit_program_label = tk.Label(options_window, image=quit_program_photoimage, bg="#024762")
        quit_program_label.place(x=80, y=50)
        quit_program_label.photo = quit_program_photoimage

        # Load and display an image for the "Yes" button
        yes_button_image = Image.open("resources/yes_button.png")
        yes_photoimage = ImageTk.PhotoImage(yes_button_image)
        yes_button_label = tk.Label(options_window, image=yes_photoimage, bg="#024762")
        yes_button_label.place(x=50, y=200)
        yes_button_label.photo = yes_photoimage
        yes_button_label.bind("<Button-1>", yes_button_click)

        # Load and display an image for the "No" button
        no_button_image = Image.open("resources/no_button.png")
        no_photoimage = ImageTk.PhotoImage(no_button_image)
        no_button_label = tk.Label(options_window, image=no_photoimage, bg="#024762")
        no_button_label.place(x=260, y=205)
        no_button_label.photo = no_photoimage
        no_button_label.bind("<Button-1>", no_button_click)

    def open_tutorial_toplevel(self):
        tutorial_options_window = tk.Toplevel(self.root)
        tutorial_options_window.title("Tutorial Options")
        tutorial_options_window.geometry("500x380")
        tutorial_options_window['bg'] = "#024762"

        def yes_tutorial_button_click(event):
            tutorial_options_window.destroy()  # Close the top-level window
            self.main_menu()          # Return to the main menu

        def no_tutorial_button_click(event):
            tutorial_options_window.destroy()  # Close the top-level window

        tutorial_options_window.grab_set()  # Prevent interactions with the main window

        quit_tutorial_image = Image.open("resources/quit_tutorial?.png")
        quit_tutorial_photoimage = ImageTk.PhotoImage(quit_tutorial_image)
        quit_tutorial_label = tk.Label(tutorial_options_window, image=quit_tutorial_photoimage, bg="#024762")
        quit_tutorial_label.place(x=10, y=50)
        quit_tutorial_label.photo = quit_tutorial_photoimage

        yes_button_image = Image.open("resources/yes_button.png")
        yes_photoimage = ImageTk.PhotoImage(yes_button_image)
        yes_button_label = tk.Label(tutorial_options_window, image=yes_photoimage, bg="#024762")
        yes_button_label.place(x=50, y=200)
        yes_button_label.photo = yes_photoimage
        yes_button_label.bind("<Button-1>", yes_tutorial_button_click)

        no_button_image = Image.open("resources/no_button.png")
        no_photoimage = ImageTk.PhotoImage(no_button_image)
        no_button_label = tk.Label(tutorial_options_window, image=no_photoimage, bg="#024762")
        no_button_label.place(x=260, y=205)
        no_button_label.photo = no_photoimage
        no_button_label.bind("<Button-1>", no_tutorial_button_click)
        
    def open_settings_toplevel(self):

        # Create a new Toplevel window for tutorial options
        settings_options_window = tk.Toplevel(self.root)
        settings_options_window.title("Settings Options")
        settings_options_window.geometry("500x380")
        settings_options_window['bg'] = "#024762"

        def yes_settings_button_click(event):
            # This function is called when the "Yes" button is clicked
            settings_options_window.destroy()  # Close the top-level window
            self.main_menu()          # Return to the main menu

        def no_settings_button_click(event):
            # This function is called when the "No" button is clicked
            settings_options_window.destroy()  # Close the top-level window

        settings_options_window.grab_set()  # Prevent interactions with the main window

        # Load and display an image for quitting the tutorial
        quit_settings_image = Image.open("resources/quit_settings?.png")
        quit_settings_photoimage = ImageTk.PhotoImage(quit_settings_image)
        quit_settings_label = tk.Label(settings_options_window, image=quit_settings_photoimage, bg="#024762")
        quit_settings_label.place(x=7, y=50)
        quit_settings_label.photo = quit_settings_photoimage

        # Load and display an image for the "Yes" button
        yes_button_image = Image.open("resources/yes_button.png")
        yes_photoimage = ImageTk.PhotoImage(yes_button_image)
        yes_button_label = tk.Label(settings_options_window, image=yes_photoimage, bg="#024762")
        yes_button_label.place(x=50, y=200)
        yes_button_label.photo = yes_photoimage
        yes_button_label.bind("<Button-1>", yes_settings_button_click)

        # Load and display an image for the "No" button
        no_button_image = Image.open("resources/no_button.png")
        no_photoimage = ImageTk.PhotoImage(no_button_image)
        no_button_label = tk.Label(settings_options_window, image=no_photoimage, bg="#024762")
        no_button_label.place(x=260, y=205)
        no_button_label.photo = no_photoimage
        no_button_label.bind("<Button-1>", no_settings_button_click)

    def open_github_link(self):
        # Opens Github link for this project for sharing
        webbrowser.open("https://github.com/minjekim12/AS91901-91906-91907",new=1) # Creates a new tab on the user's default browser

class SpellingGame:
    def __init__(self, root, game_duration):
        # Initialize the SpellingGame class with the provided root window and game duration
        self.root = root
        self.root.title("Spelling Game")

        # Initialise attributes
        self.score = 0
        self.time_left = game_duration  # Use the provided game duration
        self.game_duration = game_duration
        self.timer_running = False  # New attribute to track the timer status

        # Create and place labels to display a random letter, player's score, and remaining time
        self.letter_label = tk.Label(root, text="", font=("DIN Alternate", 40),bg="#98eaf4", fg="black", borderwidth=0,highlightbackground="white")
        self.letter_label.place(x=275, y=50)
        
        self.score_label = tk.Label(root, text="Score: 0", font=("DIN Alternate", 24),bg="#98eaf4", fg="black", borderwidth=0,highlightbackground="white")
        self.score_label.place(x=300, y=110)
        
        self.timer_label = tk.Label(root, text="Time left: 60", font=("DIN Alternate", 24), bg="#98eaf4", fg="black", borderwidth=0,highlightbackground="white")
        self.timer_label.place(x=550, y=110)
        
        # Create an entry widget for the player to input words
        self.entry = tk.Entry(root, font=("DIN Alternate", 55), bg="white", fg="black", borderwidth=0,highlightbackground="white", width=15)
        self.entry.place(x=280, y=190)
        self.entry.bind('<Return>', self.check_word)

        # Create a "PASS" button to skip the current letter
        self.pass_button = tk.Button(root, text="PASS", font=("DIN Alternate", 40), bg="white", fg="black", borderwidth=0,highlightbackground="white", width=9, command=self.pass_prompt)
        self.pass_button.place(x=376, y=350)

        # Store the game status
        self.in_game_page = False

        # Create a button to open game options
        self.game_options_button = tk.Button(
            root,
            text="X",
            font=("DIN Alternate", 20),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
            command=self.open_game_toplevel,  # Call the method to open the options window
        )
        self.game_options_button.place(x=20, y=20)

        # Initialize the game by updating the displayed letter, starting the countdown timer, and playing background music
        self.update_letter()
        self.update_letter()
        self.countdown()
        self.play_bgm()

    # Initialize the pygame mixer
    pygame.mixer.init()

    def play_bgm(self):
        # Load and play background music in an infinite loop (-1 = infinite loops)
        pygame.mixer.music.load("resources/background_music.mp3")
        pygame.mixer.music.play(loops = -1)


    def start_timer(self):
        # Start the game timer if it's not already running
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def stop_timer(self):
        # Stop the game timer
        self.timer_running = False

    def update_letter(self):
        # Generate a random letter and word length
        self.letter = random.choice(string.ascii_uppercase)
        self.word_length = random.randint(3, 6)

        # Update the displayed letter and word length on the label
        self.letter_label.config(text=f"Letter: {self.letter}  Word length: {self.word_length}")

        # Clear the text entry field
        self.entry.delete(0, tk.END)
    
    def pass_prompt(self):
        # Minus a point from the score when the player chooses to pass
        self.score -= 1
        self.update_letter() # Update the displayed letter and word length
        self.score_label.config(text=f"Score: {self.score}")

    def countdown(self):  
        # Only run the countdown if in game page
        if self.time_left > 0 and self.timer_running:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        elif self.time_left == 0 and self.timer_running:
            self.finish_game()

    def check_word(self, event):
        # This method is called when the player presses Enter in the text entry field
        user_word = self.entry.get()

        if len(user_word) == self.word_length and user_word[0].lower() == self.letter.lower():
            # Check if the entered word is of the correct length and starts with the given letter
            if self.is_valid_word(user_word.lower()):
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.update_letter()
            else:
                messagebox.showinfo("Invalid Word", "Please enter a valid English word.")
        else:
            if len(user_word) != self.word_length:
                messagebox.showinfo("Invalid Input", f"Please enter a word with {self.word_length} letters.")
            elif user_word[0].lower() != self.letter.lower():
                messagebox.showinfo("Invalid Input", f"Please enter a word that starts with the letter {self.letter}.")

        self.entry.delete(0, tk.END) # Clear the text entry field after checking the word

    def is_valid_word(self, word):
        # This method checks if the provided word is in the list of valid words
        with open('valid_words.txt', 'r') as word_file:
            valid_words = set(word.strip().lower() for word in word_file)
        return word in valid_words

    def start_game(self):
        # This method is called to start the game. It sets up the initial conditions.
        self.root.after(0, self.start_timer)  # Start the timer when the game starts
        self.update_letter()


    def finish_game(self):
        # This method is called when the game ends, either due to time running out or the player choosing to quit.
        self.entry.config(state="disabled")
        self.stop_timer()
        pygame.mixer.music.stop()
        
        # Determine the message based on whether the user submitted a name
        if app.user_name:
            message = f"Game Over, {app.user_name}!\nYour score: {self.score}\n\nRestart the game?"
        else:
            message = f"Game Over!\nYour score: {self.score}\n\nRestart the game?"

        # Display a message box with the game over message and options to restart or go to the main menu
        choice = messagebox.askquestion("Game Over", message, icon="info")
        
        if choice == "yes":
            self.restart_game()
        else:
            self.go_to_main_menu()

    def restart_game(self):
        # This method is called to restart the game.
        # It resets all game values to their initial values and starts the timer.
        self.entry.config(state="normal")
        self.score = 0
        self.time_left = self.game_duration  
        self.update_letter()
        self.score_label.config(text="Score: 0")
        self.timer_label.config(text=f"Time left: {self.time_left}")
        self.entry.delete(0, tk.END)
        self.timer_running = True  
        self.countdown()
        pygame.mixer.music.play()
 
    def go_to_main_menu(self):
        # This method is called to return to the main menu.
        # It stops the timer, goes back to the main menu, and resets game values.
        self.stop_timer()  # Stop the timer when going back to the main menu
        app.main_menu()
        self.in_game_page = False
        self.time_left = 60 
        pygame.mixer.music.stop()

   

    def open_game_toplevel(self):
        # Create a top-level window for game options
        game_options_window = tk.Toplevel(self.root)
        game_options_window.title("Game Options")
        game_options_window.geometry("500x380")
        game_options_window['bg'] = "#024762"

        # Callback function for the "Yes" button to return to the main menu
        def yes_tutorial_button_click(event):
            game_options_window.destroy()  # Close the top-level window
            self.go_to_main_menu()          # Return to the main menu

        # Callback function for the "No" button to close the top-level window
        def no_tutorial_button_click(event):
            game_options_window.destroy()  # Close the top-level window

        game_options_window.grab_set()  # Prevent interactions with the main window
        
        # Load and display the "Quit Game" image
        quit_game_image = Image.open("resources/quit_game_new.png")
        quit_game_photoimage = ImageTk.PhotoImage(quit_game_image)
        quit_game_label = tk.Label(game_options_window, image=quit_game_photoimage, bg="#024762")
        quit_game_label.place(x=80, y=50)
        quit_game_label.photo = quit_game_photoimage

        # Create and configure the "Yes" button
        yes_button_image = Image.open("resources/yes_button.png")
        yes_photoimage = ImageTk.PhotoImage(yes_button_image)
        yes_button_label = tk.Label(game_options_window, image=yes_photoimage, bg="#024762")
        yes_button_label.place(x=50, y=200)
        yes_button_label.photo = yes_photoimage
        yes_button_label.bind("<Button-1>", yes_tutorial_button_click)

        # Create and configure the "No" button
        no_button_image = Image.open("resources/no_button.png")
        no_photoimage = ImageTk.PhotoImage(no_button_image)
        no_button_label = tk.Label(game_options_window, image=no_photoimage, bg="#024762")
        no_button_label.place(x=260, y=205)
        no_button_label.photo = no_photoimage
        no_button_label.bind("<Button-1>", no_tutorial_button_click)
        

# Create an instance of the main application
root = tk.Tk()
app = SpellCraftApp(root)
root.mainloop()