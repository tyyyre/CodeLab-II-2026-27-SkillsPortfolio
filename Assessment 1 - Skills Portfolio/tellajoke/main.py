
import tkinter as tk
from tkinter import messagebox
import random
import os

# Create the main application window
root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("650x500")
root.resizable(False, False)
root.configure(bg="#152238")

# Colours used in the application
background_color = "#152238"
button_color = "#2874A6"
text_color = "white"

# Store the jokes and current punchline
jokes = []
current_punchline = ""


# Function to load jokes from the text file
def loadJokes():
    jokes_list = []

    # Find the folder where main.py is saved
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Create the full path to randomJokes.txt
    file_path = os.path.join(folder_path, "randomJokes.txt")

    try:
        # Open the file and read each joke
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Ignore empty lines
                if line:
                    jokes_list.append(line)

    except FileNotFoundError:
        messagebox.showerror(
            "File Error",
            "randomJokes.txt could not be found."
        )

    return jokes_list


# Function to display a random joke
def displayJoke():
    global current_punchline

    # Check if any jokes are available
    if not jokes:
        messagebox.showwarning(
            "No Jokes",
            "There are no jokes available."
        )
        return

    # Select a random joke
    selected_joke = random.choice(jokes)

    # Separate the joke question and punchline
    if "?" in selected_joke:
        question, punchline = selected_joke.split("?", 1)

        question = question.strip() + "?"
        current_punchline = punchline.strip()
    else:
        question = selected_joke
        current_punchline = ""

    # Display the joke question
    joke_label.config(text=question)

    # Hide the previous punchline
    punchline_label.config(text="")

    # Enable the punchline button
    punchline_button.config(state="normal")


# Function to reveal the punchline
def showPunchline():
    if current_punchline:
        punchline_label.config(
            text=current_punchline
        )

        # Disable button after showing the punchline
        punchline_button.config(state="disabled")

    else:
        messagebox.showinfo(
            "Joke Teller",
            "Please select a joke first."
        )


# Function to display the welcome screen
def displayWelcome():
    global joke_label, punchline_label, punchline_button

    # Application title
    title_label = tk.Label(
        root,
        text="Alexa Tell Me a Joke",
        font=("Arial", 24, "bold"),
        bg=background_color,
        fg=text_color
    )
    title_label.pack(pady=30)

    # Welcome message
    welcome_label = tk.Label(
        root,
        text="Welcome! Ready for some jokes?",
        font=("Arial", 15),
        bg=background_color,
        fg=text_color
    )
    welcome_label.pack(pady=10)

    # Button to select a random joke
    joke_button = tk.Button(
        root,
        text="Tell Me a Joke",
        font=("Arial", 13),
        bg=button_color,
        fg="white",
        width=20,
        command=displayJoke
    )
    joke_button.pack(pady=15)

    # Label to display the joke question
    joke_label = tk.Label(
        root,
        text="Your joke will appear here!",
        font=("Arial", 15),
        bg=background_color,
        fg=text_color,
        wraplength=550,
        justify="center"
    )
    joke_label.pack(pady=15)

    # Button to reveal the punchline
    punchline_button = tk.Button(
        root,
        text="Show Punchline",
        font=("Arial", 13),
        bg=button_color,
        fg="white",
        width=20,
        state="disabled",
        command=showPunchline
    )
    punchline_button.pack(pady=15)

    # Label to display the punchline
    punchline_label = tk.Label(
        root,
        text="",
        font=("Arial", 14, "bold"),
        bg=background_color,
        fg="#58D68D",
        wraplength=550,
        justify="center"
    )
    punchline_label.pack(pady=15)


# Load jokes when the application starts
jokes = loadJokes()

# Display the welcome screen
displayWelcome()

# Keep the application running
root.mainloop()
