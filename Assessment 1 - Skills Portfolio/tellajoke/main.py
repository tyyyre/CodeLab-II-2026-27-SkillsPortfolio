
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


# Call the welcome function
displayWelcome()

# Keep the window running
root.mainloop()
