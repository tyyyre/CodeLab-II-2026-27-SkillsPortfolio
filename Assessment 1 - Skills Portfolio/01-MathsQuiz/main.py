
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

# Quiz variables
min_number = 1
max_number = 9
question_number = 0
score = 0
first_number = 0
second_number = 0
operation = "+"
correct_answer = 0
attempts = 0


# Remove all widgets from the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Display the difficulty selection menu
def displayMenu():
    clear_window()

    tk.Label(
        root,
        text="MATHS QUIZ",
        font=("Arial", 28, "bold"),
        bg=BG_COLOR,
        fg=FG_COLOR
    ).pack(pady=35)

    tk.Label(
        root,
        text="Select Your Difficulty Level",
        font=("Arial", 16),
        bg=BG_COLOR,
        fg=FG_COLOR
    ).pack(pady=15)

    # Difficulty levels and their number ranges
    difficulties = [
        ("Easy", 1, 9),
        ("Moderate", 10, 99),
        ("Advanced", 1000, 9999)
    ]

    for name, minimum, maximum in difficulties:
        tk.Button(
            root,
            text=name,
            font=("Arial", 14, "bold"),
            width=20,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            command=lambda low=minimum, high=maximum:
                startQuiz(low, high)
        ).pack(pady=8)


# Generate a random number
def randomInt(minimum, maximum):
    return random.randint(minimum, maximum)


# Randomly select addition or subtraction
def decideOperation():
    return random.choice(["+", "-"])


# Start the quiz with the selected difficulty
def startQuiz(minimum, maximum):
    global min_number, max_number
    global question_number, score, attempts

    min_number = minimum
    max_number = maximum

    # Reset quiz values
    question_number = 0
    score = 0
    attempts = 0

    displayProblem()


# Display the current maths question
def displayProblem():
    global first_number, second_number
    global operation, correct_answer, attempts

    clear_window()

    # Generate random numbers and operation
    first_number = randomInt(min_number, max_number)
    second_number = randomInt(min_number, max_number)
    operation = decideOperation()

    # Calculate the correct answer
    if operation == "+":
        correct_answer = first_number + second_number
    else:
        correct_answer = first_number - second_number

    attempts = 0

    # Question heading
    tk.Label(
        root,
        text="MATHS QUIZ",
        font=("Arial", 24, "bold"),
        bg=BG_COLOR,
        fg=FG_COLOR
    ).pack(pady=20)

    # Display question number and score
    tk.Label(
        root,
        text=f"Question {question_number + 1} of 10",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=FG_COLOR
    ).pack(pady=5)

    tk.Label(
        root,
        text=f"Score: {score}/100",
        font=("Arial", 13, "bold"),
        bg=BG_COLOR,
        fg="#FFD700"
    ).pack(pady=5)

    # Display the maths problem
    tk.Label(
        root,
        text=f"{first_number} {operation} {second_number} = ?",
        font=("Arial", 30, "bold"),
        bg=BG_COLOR,
        fg=FG_COLOR
    ).pack(pady=25)

    # Answer input field
    global answer_entry
    answer_entry = tk.Entry(
        root,
        font=("Arial", 18),
        justify="center",
        width=15
    )
    answer_entry.pack(pady=10)
    answer_entry.focus()

    # Submit answer button
    tk.Button(
        root,
        text="Submit Answer",
        font=("Arial", 13, "bold"),
        bg=BUTTON_COLOR,
        fg=FG_COLOR,
        width=18,
        command=checkAnswer
    ).pack(pady=10)

    # Feedback label
    global feedback_label
    feedback_label = tk.Label(
        root,
        text="Enter your answer above",
        font=("Arial", 12),
        bg=BG_COLOR,
        fg=FG_COLOR
    )
    feedback_label.pack(pady=5)


# Check the user's answer
def checkAnswer():
    global attempts, score, question_number

    user_answer = answer_entry.get()

    # Check that the user entered a number
    try:
        user_answer = int(user_answer)
    except ValueError:
        feedback_label.config(
            text="Please enter a valid number!",
            fg="#FF6666"
        )
        return

    attempts += 1

    if user_answer == correct_answer:
        isCorrect(True)
        question_number += 1

        if question_number == 10:
            messagebox.showinfo(
                "Quiz Complete",
                f"You have completed all 10 questions!\n"
                f"Your score is {score}/100"
            )
            displayMenu()
        else:
            root.after(1200, displayProblem)

    else:
        if attempts == 1:
            isCorrect(False)
            feedback_label.config(
                text="Wrong answer! Try one more time.",
                fg="#FF6666"
            )
            answer_entry.delete(0, tk.END)
        else:
            feedback_label.config(
                text=f"Incorrect! The answer was {correct_answer}.",
                fg="#FF6666"
            )

            question_number += 1

            if question_number == 10:
                messagebox.showinfo(
                    "Quiz Complete",
                    f"You have completed all 10 questions!\n"
                    f"Your score is {score}/100"
                )
                displayMenu()
            else:
                root.after(1500, displayProblem)


# Display whether the answer is correct
def isCorrect(correct):
    global score

    if correct:
        if attempts == 1:
            score += 10
            feedback_label.config(
                text="Correct! You earned 10 points.",
                fg="#66FF99"
            )
        else:
            score += 5
            feedback_label.config(
                text="Correct! You earned 5 points.",
                fg="#66FF99"
            )


# Display the initial menu
displayMenu()

# Run the application
root.mainloop()
