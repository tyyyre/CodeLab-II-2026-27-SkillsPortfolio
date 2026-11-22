
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

    # Button to get a random joke
    joke_button = tk.Button(
        root,
        text="Tell Me a Joke",
        font=("Arial", 13),
        bg="#2874A6",
        fg="white",
        command=displayJoke
    )
    joke_button.pack(pady=15)
        # Display the joke question below the button
    joke_label.pack(pady=10)

    # Display the punchline below the question
    punchline_label.pack(pady=10)



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

# Function to display a random joke
def displayJoke():
    global current_punchline

    if not jokes:
        messagebox.showwarning(
            "No Jokes",
            "There are no jokes available."
        )
        return

    # Select a random joke from the list
    selected_joke = random.choice(jokes)

    # Separate the question and punchline
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

# Load all jokes into a list
jokes = loadJokes()

# Store the current joke's punchline
current_punchline = ""

# Label to display the joke question
joke_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#152238",
    fg="white",
    wraplength=500
)

# Label to display the punchline later
punchline_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#152238",
    fg="#58D68D",
    wraplength=500
)


# Call the welcome function
displayWelcome()

# Keep the window running
root.mainloop()
