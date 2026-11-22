
import tkinter as tk
from tkinter import messagebox
import random
import os

# Sky Blue theme colours
BG_COLOR = "#F0F5FF"
CHAT_COLOR = "#DCE7FA"
BLUE_COLOR = "#3478D4"
TEXT_COLOR = "#253A59"
GREY_COLOR = "#64748B"
WHITE = "#FFFFFF"

# Create the main window
root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("650x650")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# Store the jokes and current conversation
jokes = []
current_punchline = ""
current_response = ""

# Human responses for the different jokes
# These match the order of the jokes in randomJokes.txt
human_responses = [
    "Why?",                  # Chicken
    "What happens?",         # Clown
    "Why?",                  # Car
    "How?",                  # Hipster
    "What did he say?",      # Janitor
    "No, what happened?",    # Band
    "Why?",                  # Golfer
    "Why?",                  # Maths
    "Why?",                  # Pirates
    "Why?",                  # Mushroom
    "Why?",                  # Bananas
    "What did he say?",      # Buffalo
    "Why not?",              # Cornfield
    "What?",                 # Carbs
    "Why?",                  # Can crusher
    "Why?",                  # Birthday boy
    "What?",                 # House
    "Why?",                  # Toilet paper
    "Why?",                  # Bike
    "Sure, tell me!",        # Pizza
    "Why?",                  # Chemists
    "Why?",                  # Desert
    "What did it say?",      # Cheese
    "Why?",                  # Developer
    "Really? Why?",          # Ants
    "Why?",                  # Donut
    "What?",                 # Bear
    "What?",                 # Zombie
    "What?",                 # Dinosaur
    "Why?",                  # Tennis
    "What did it say?",      # Glass
    "What?",                 # Potato
    "What did it say?",      # Ocean
    "What did it say?",      # Eyes
    "What?",                 # Dog
    "What's the difference?",# Hippo and Zippo
    "Why?"                   # Atoms
]


# Load jokes from the text file
def loadJokes():
    jokes_list = []

    # Find the folder containing main.py
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "randomJokes.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Split each joke into setup and punchline
                if "?" in line:
                    setup, punchline = line.split("?", 1)

                    # Store the two parts together
                    jokes_list.append(
                        (setup.strip() + "?", punchline.strip())
                    )

    except FileNotFoundError:
        messagebox.showerror(
            "File Error",
            "randomJokes.txt could not be found."
        )

    return jokes_list



# Create a chat message with a small sender name
def createMessage(sender, message):

    # Choose colours and alignment for each sender
    if sender == "Alexa":
        bubble_color = CHAT_COLOR
        font_color = TEXT_COLOR
        side = "w"
        sender_name = "alexa"
    else:
        bubble_color = BLUE_COLOR
        font_color = WHITE
        side = "e"
        sender_name = "hamza"

    # Create a container for the message
    message_frame = tk.Frame(
        chat_frame,
        bg=BG_COLOR
    )
    message_frame.pack(
        fill="x",
        padx=15,
        pady=5
    )

    # Display the sender's name in a smaller font
    name_label = tk.Label(
        message_frame,
        text=sender_name,
        font=("Georgia", 9, "italic"),
        bg=BG_COLOR,
        fg=GREY_COLOR
    )
    name_label.pack(anchor=side, padx=8, pady=(0, 3))

    # Display the actual message in a separate bubble
    bubble = tk.Label(
        message_frame,
        text=message,
        font=("Arial", 12),
        bg=bubble_color,
        fg=font_color,
        wraplength=440,
        justify="left",
        padx=15,
        pady=10
    )
    bubble.pack(anchor=side)


# Select and display a random joke
def displayJoke():
    global current_punchline, current_response

    if not jokes:
        messagebox.showwarning(
            "No Jokes",
            "No jokes are available."
        )
        return

    # Remove the previous conversation
    for widget in chat_frame.winfo_children():
        widget.destroy()

    # Randomly select a joke using its position
    joke_index = random.randrange(len(jokes))

    setup, punchline = jokes[joke_index]

    current_punchline = punchline

    # Choose the matching human response
    if joke_index < len(human_responses):
        current_response = human_responses[joke_index]
    else:
        current_response = "What?"

    # Display Alexa's joke setup
    createMessage("Alexa", setup)

    # Change the response button text
    response_button.config(
        text=current_response,
        state="normal"
    )

    # Hide the starting button
    start_button.pack_forget()

    # Show the conversation buttons
    response_button.pack(pady=10)
    next_button.pack(pady=7)


# Show the human response and Alexa's punchline
def showPunchline():
    if current_punchline:
        # Display what the human says
        createMessage("You", current_response)

        # Display Alexa's punchline
        createMessage("Alexa", current_punchline)

        # Prevent the response from being clicked twice
        response_button.config(state="disabled")


# Display another random joke
def nextJoke():
    displayJoke()


# Close the application
def quitApp():
    root.destroy()


# Create the heading
header = tk.Frame(
    root,
    bg=WHITE,
    height=75
)
header.pack(fill="x")

tk.Label(
    header,
    text="Alexa Joke Teller",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=TEXT_COLOR
).pack(pady=(12, 2))

tk.Label(
    header,
    text="Your interactive joke assistant",
    font=("Arial", 10),
    bg=WHITE,
    fg=GREY_COLOR
).pack()


# Create the chat area
chat_frame = tk.Frame(
    root,
    bg=BG_COLOR,
    height=310
)
chat_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)
chat_frame.pack_propagate(False)


# Starting message
createMessage(
    "Alexa",
    "Hello! Ready for a joke?"
)


# Create the buttons area
button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)
button_frame.pack(pady=10)


# Button shown when the application first opens
start_button = tk.Button(
    button_frame,
    text="Alexa tell me a Joke",
    font=("Arial", 13, "bold"),
    bg=BLUE_COLOR,
    fg=WHITE,
    width=24,
    command=displayJoke
)
start_button.pack(pady=10)


# Human response button (hidden at first)
response_button = tk.Button(
    button_frame,
    text="Why?",
    font=("Arial", 12),
    bg=BLUE_COLOR,
    fg=WHITE,
    width=24,
    command=showPunchline
)


# Next Joke button (hidden at first)
next_button = tk.Button(
    button_frame,
    text="Next Joke",
    font=("Arial", 12),
    bg=BLUE_COLOR,
    fg=WHITE,
    width=24,
    command=nextJoke
)


# Quit button is always visible
quit_button = tk.Button(
    root,
    text="Quit",
    font=("Arial", 12),
    bg="#E1E9F4",
    fg=TEXT_COLOR,
    width=24,
    command=quitApp
)
quit_button.pack(pady=(5, 15))


# Load all jokes from the text file
jokes = loadJokes()

# Keep the application running
root.mainloop()
