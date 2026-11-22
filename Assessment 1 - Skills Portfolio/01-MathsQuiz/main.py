
import tkinter as tk
from tkinter import messagebox
import random

# Main application window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x450")
root.resizable(False, False)

# Application colours
BG_COLOR = "#172033"
FG_COLOR = "#FFFFFF"
BUTTON_COLOR = "#4169E1"

root.configure(bg=BG_COLOR)


# Clear existing widgets
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Display difficulty menu
def displayMenu():
    clear_window()

    title = tk.Label(
        root,
        text="MATHS QUIZ",
        font=("Arial", 28, "bold"),
        bg=BG_COLOR,
        fg=FG_COLOR
    )
    title.pack(pady=35)

    instruction = tk.Label(
        root,
        text="Select Your Difficulty Level",
        font=("Arial", 16),
        bg=BG_COLOR,
        fg=FG_COLOR
    )
    instruction.pack(pady=15)

    difficulties = [
        ("Easy", 1, 9),
        ("Moderate", 10, 99),
        ("Advanced", 1000, 9999)
    ]

    for name, minimum, maximum in difficulties:
        button = tk.Button(
            root,
            text=name,
            font=("Arial", 14, "bold"),
            width=20,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            command=lambda low=minimum, high=maximum:
                startQuiz(low, high)
        )
        button.pack(pady=8)


# Generate random number
def randomInt(minimum, maximum):
    return random.randint(minimum, maximum)


# Randomly select addition or subtraction
def decideOperation():
    return random.choice(["+", "-"])


# Start quiz
def startQuiz(minimum, maximum):
    global min_number, max_number

    min_number = minimum
    max_number = maximum

    messagebox.showinfo(
        "Maths Quiz",
        "Your quiz is starting!"
    )

    displayMenu()


# Display initial menu
displayMenu()

# Run application
root.mainloop()
