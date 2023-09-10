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
import random
import string
from tkinter import messagebox
import pygame

class SpellCraftApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpellCraft")

        self.window_width = 960
        self.window_height = 540
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        self.root.resizable(False, False)
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}")

        self.main_menu()

    def main_menu(self):
        self.mainmenu_open = Image.open("resources/main_menu_bg.png")
        self.mainmenu_bg = ImageTk.PhotoImage(self.mainmenu_open)
        self.main_menu_bg_label = tk.Label(self.root, image=self.mainmenu_bg)
        self.main_menu_bg_label.place(x=0, y=0)

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
        self.main_menu_bg_label.destroy()
        self.game_description_label.destroy()
        self.tutorial_button.destroy()
        self.game_start_button.destroy()
        self.settings_button.destroy()
        self.tutorial_open = Image.open("resources/tutorial_bg.png")
        self.tutorial_bg = ImageTk.PhotoImage(self.tutorial_open)
        self.tutorial_bg_label = tk.Label(self.root, image=self.tutorial_bg)
        self.tutorial_bg_label.place(x=0, y=0)

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
        self.main_menu_bg_label.destroy()
        self.game_description_label.destroy()
        self.tutorial_button.destroy()
        self.game_start_button.destroy()
        self.settings_button.destroy()
        self.settings_open = Image.open("resources/settings_bg.png")
        self.settings_bg = ImageTk.PhotoImage(self.settings_open)
        self.settings_bg_label = tk.Label(self.root, image=self.settings_bg)
        self.settings_bg_label.place(x=0, y=0)

        self.open_settings_toplevel_button = tk.Button(
            self.root,
            text="X",
            font=("DIN Alternate", 20),
            bg="blue",
            padx=7,
            pady=5,
            borderwidth=0,
            highlightbackground="#98eaf4",
        )
        self.open_settings_toplevel_button.place(x=20, y=20)

    def start_game(self):
        self.main_menu_bg_label.destroy()
        self.game_description_label.destroy()
        self.tutorial_button.destroy()
        self.game_start_button.destroy()
        self.settings_button.destroy()
        self.game_bg_open = Image.open("resources/game_bg.png")
        self.game_bg = ImageTk.PhotoImage(self.game_bg_open)
        self.game_bg_label = tk.Label(self.root, image=self.game_bg)
        self.game_bg_label.place(x=0, y=0)
        game = SpellingGame(self.root)
        self.in_game_page = True
        game.start_game()  # Start the game and the timer


    def open_toplevel(self):
        options_window = tk.Toplevel(root)
        options_window.title("Options")
        options_window.geometry("500x380")
        options_window['bg'] = "#024762"

        def yes_button_click(event):
            print("Button clicked")
            root.destroy()

        def no_button_click(event):
            print("noButton clicked")
            options_window.destroy()

        options_window.grab_set()  # Prevent interactions with the main window

        quit_program_image = Image.open("resources/quit_program?.png")
        quit_program_photoimage = ImageTk.PhotoImage(quit_program_image)
        quit_program_label = tk.Label(options_window, image=quit_program_photoimage, bg="#024762")
        quit_program_label.place(x=80, y=50)
        quit_program_label.photo = quit_program_photoimage

        yes_button_image = Image.open("resources/yes_button.png")
        yes_photoimage = ImageTk.PhotoImage(yes_button_image)
        yes_button_label = tk.Label(options_window, image=yes_photoimage, bg="#024762")
        yes_button_label.place(x=50, y=200)
        yes_button_label.photo = yes_photoimage
        yes_button_label.bind("<Button-1>", yes_button_click)

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

        def yes_game_button_click(event):
            tutorial_options_window.destroy()  # Close the top-level window
            self.main_menu()          # Return to the main menu

        def no_game_button_click(event):
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
        yes_button_label.bind("<Button-1>", yes_game_button_click)

        no_button_image = Image.open("resources/no_button.png")
        no_photoimage = ImageTk.PhotoImage(no_button_image)
        no_button_label = tk.Label(tutorial_options_window, image=no_photoimage, bg="#024762")
        no_button_label.place(x=260, y=205)
        no_button_label.photo = no_photoimage
        no_button_label.bind("<Button-1>", no_game_button_click)
        

class SpellingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Game")

        
        
        self.score = 0
        self.time_left = 60
        self.timer_running = False  # New attribute to track the timer status
        
        
        self.letter_label = tk.Label(root, text="", font=("DIN Alternate", 40),bg="#98eaf4", fg="black", borderwidth=0,highlightbackground="white")
        self.letter_label.place(x=275, y=50)
        
        self.score_label = tk.Label(root, text="Score: 0", font=("DIN Alternate", 24),bg="#98eaf4", fg="black", borderwidth=0,highlightbackground="white")
        self.score_label.place(x=300, y=110)
        
        self.timer_label = tk.Label(root, text="Time left: 60", font=("DIN Alternate", 24), bg="#98eaf4", fg="black", borderwidth=0,highlightbackground="white")
        self.timer_label.place(x=550, y=110)
        
        self.entry = tk.Entry(root, font=("DIN Alternate", 55), bg="white", fg="black", borderwidth=0,highlightbackground="white", width=15)
        self.entry.place(x=280, y=190)
        self.entry.bind('<Return>', self.check_word)

        self.pass_button = tk.Button(root, text="PASS", font=("DIN Alternate", 40), bg="white", fg="black", borderwidth=0,highlightbackground="white", width=9, command=self.pass_prompt)
        self.pass_button.place(x=376, y=350)

        # Store the game page status
        self.in_game_page = False

        
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


        self.update_letter()
        self.countdown()
        self.play_bgm()

    pygame.mixer.init()

    def play_bgm(self):
        pygame.mixer.music.load("resources/background_music.mp3")
        pygame.mixer.music.play(loops = -1)


    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def stop_timer(self):
        self.timer_running = False

    def update_letter(self):
        self.letter = random.choice(string.ascii_uppercase)
        self.word_length = random.randint(3, 6)
        self.letter_label.config(text=f"Letter: {self.letter}  Word length: {self.word_length}")
        self.entry.delete(0, tk.END)
    
    def pass_prompt(self):
        self.score -= 1
        self.update_letter()
        self.score_label.config(text=f"Score: {self.score}")

    def countdown(self):  # Only run the countdown if in game page
            if self.time_left > 0 and self.timer_running:
                self.timer_label.config(text=f"Time left: {self.time_left}")
                self.time_left -= 1
                self.root.after(1000, self.countdown)
            elif self.time_left == 0 and self.timer_running:
                self.finish_game()

    def check_word(self, event):
        user_word = self.entry.get()

        if len(user_word) == self.word_length and user_word[0].lower() == self.letter.lower():
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

        self.entry.delete(0, tk.END)

    def is_valid_word(self, word):
        with open('valid_words.txt', 'r') as word_file:
            valid_words = set(word.strip().lower() for word in word_file)
        return word in valid_words

    def start_game(self):
        self.root.after(0, self.start_timer)  # Start the timer when the game starts
        self.update_letter()

    def finish_game(self):
        self.entry.config(state="disabled")
        self.stop_timer()
        pygame.mixer.music.stop()
        
        # Display a messagebox with score and options
        choice = messagebox.askquestion("Game Over", f"Your score: {self.score}\n\nRestart the game?", icon="info")
        
        if choice == "yes":
            self.restart_game()
        else:
            self.go_to_main_menu()

    def restart_game(self):
        self.entry.config(state="normal")
        self.score = 0
        self.time_left = 60  # Reset the timer to its initial value
        self.update_letter()
        self.score_label.config(text="Score: 0")
        self.timer_label.config(text="Time left: 60")
        self.entry.delete(0, tk.END)
        self.countdown()
        pygame.mixer.music.play()
 
    def go_to_main_menu(self):
        self.stop_timer()  # Stop the timer when going back to the main menu
        app.main_menu()
        self.in_game_page = False
        self.time_left = 60  # Reset the timer to its initial value 
        pygame.mixer.music.stop()

    # Inside the SpellingGame class

    def open_game_toplevel(self):
        game_options_window = tk.Toplevel(self.root)
        game_options_window.title("Game Options")
        game_options_window.geometry("500x380")
        game_options_window['bg'] = "#024762"

        def yes_game_button_click(event):
            game_options_window.destroy()  # Close the top-level window
            self.go_to_main_menu()          # Return to the main menu

        def no_game_button_click(event):
            game_options_window.destroy()  # Close the top-level window

        game_options_window.grab_set()  # Prevent interactions with the main window

        quit_game_image = Image.open("resources/quit_game_new.png")
        quit_game_photoimage = ImageTk.PhotoImage(quit_game_image)
        quit_game_label = tk.Label(game_options_window, image=quit_game_photoimage, bg="#024762")
        quit_game_label.place(x=80, y=50)
        quit_game_label.photo = quit_game_photoimage

        yes_button_image = Image.open("resources/yes_button.png")
        yes_photoimage = ImageTk.PhotoImage(yes_button_image)
        yes_button_label = tk.Label(game_options_window, image=yes_photoimage, bg="#024762")
        yes_button_label.place(x=50, y=200)
        yes_button_label.photo = yes_photoimage
        yes_button_label.bind("<Button-1>", yes_game_button_click)

        no_button_image = Image.open("resources/no_button.png")
        no_photoimage = ImageTk.PhotoImage(no_button_image)
        no_button_label = tk.Label(game_options_window, image=no_photoimage, bg="#024762")
        no_button_label.place(x=260, y=205)
        no_button_label.photo = no_photoimage
        no_button_label.bind("<Button-1>", no_game_button_click)
    

    

        
    


# Main Window Properties
root = tk.Tk()
app = SpellCraftApp(root)
root.mainloop()
