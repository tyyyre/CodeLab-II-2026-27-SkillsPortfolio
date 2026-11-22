
import tkinter as tk
from tkinter import messagebox
import random

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Alexa Tell Me a Joke")

# Set the window size
root.geometry("600x450")

# Prevent the window from being resized
root.resizable(False, False)

# Set the background colour
root.configure(bg="#152238")


# Function to display the welcome screen
def displayWelcome():
    # Display the application title
    title_label = tk.Label(
        root,
        text="Alexa Tell Me a Joke",
        font=("Arial", 24, "bold"),
        bg="#152238",
        fg="white"
    )
    title_label.pack(pady=40)

    # Display a welcome message
    welcome_label = tk.Label(
        root,
        text="Welcome! Ready for some jokes?",
        font=("Arial", 15),
        bg="#152238",
        fg="white"
    )
    welcome_label.pack(pady=20)


# Function to read jokes from the text file
def loadJokes():
    jokes = []

    try:
        # Open the jokes file
        with open("randomJokes.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Ignore empty lines
                if line:
                    jokes.append(line)

    except FileNotFoundError:
        messagebox.showerror(
            "File Error",
            "randomJokes.txt could not be found."
        )

    return jokes

# Load all jokes into a list
jokes = loadJokes()

# Call the welcome function
displayWelcome()

# Keep the window running
root.mainloop()
