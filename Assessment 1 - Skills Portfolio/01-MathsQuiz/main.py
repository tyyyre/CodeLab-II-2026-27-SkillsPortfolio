
import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#152238")

# Quiz variables
min_number = 1
max_number = 9
question_number = 0
score = 0
attempts = 0
correct_answer = 0

# Used to manage the next question
next_question_timer = None
quiz_active = False

# Window colours
background_color = "#152238"
button_color = "#2874A6"
text_color = "white"


# Remove everything from the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Cancel any question that is waiting to appear
def cancel_timer():
    global next_question_timer

    if next_question_timer is not None:
        root.after_cancel(next_question_timer)
        next_question_timer = None


# Show the home menu
def displayMenu():
    global quiz_active

    quiz_active = False
    cancel_timer()
    clear_window()

    tk.Label(
        root,
        text="Welcome to Maths Quiz",
        font=("Arial", 24, "bold"),
        bg=background_color,
        fg=text_color
    ).pack(pady=35)

    tk.Label(
        root,
        text="Choose Your Difficulty Level",
        font=("Arial", 15),
        bg=background_color,
        fg=text_color
    ).pack(pady=15)

    # Easy difficulty
    tk.Button(
        root,
        text="Easy",
        font=("Arial", 14),
        bg=button_color,
        fg="white",
        width=20,
        command=lambda: startQuiz(1, 9)
    ).pack(pady=10)

    # Moderate difficulty
    tk.Button(
        root,
        text="Moderate",
        font=("Arial", 14),
        bg=button_color,
        fg="white",
        width=20,
        command=lambda: startQuiz(10, 99)
    ).pack(pady=10)

    # Advanced difficulty
    tk.Button(
        root,
        text="Advanced",
        font=("Arial", 14),
        bg=button_color,
        fg="white",
        width=20,
        command=lambda: startQuiz(1000, 9999)
    ).pack(pady=10)


# Generate a random number
def randomInt(minimum, maximum):
    return random.randint(minimum, maximum)


# Randomly select addition or subtraction
def decideOperation():
    return random.choice(["+", "-"])


# Start a new quiz
def startQuiz(minimum, maximum):
    global min_number, max_number
    global question_number, score, attempts, quiz_active

    cancel_timer()

    min_number = minimum
    max_number = maximum

    # Reset values for a new quiz
    question_number = 0
    score = 0
    attempts = 0
    quiz_active = True

    # Starting popup
    messagebox.showinfo(
        "Maths Quiz",
        "Your quiz is starting!\n\nGood luck!"
    )

    displayProblem()


# Display a maths question
def displayProblem():
    global question_number, attempts, correct_answer
    global answer_entry, feedback_label, submit_button
    global next_question_timer

    if not quiz_active:
        return

    next_question_timer = None
    clear_window()

    question_number += 1
    attempts = 0

    # Generate two random numbers
    number1 = randomInt(min_number, max_number)
    number2 = randomInt(min_number, max_number)

    operation = decideOperation()

    # Calculate the correct answer
    if operation == "+":
        correct_answer = number1 + number2
    else:
        correct_answer = number1 - number2

    tk.Label(
        root,
        text=f"Question {question_number} of 10",
        font=("Arial", 20, "bold"),
        bg=background_color,
        fg=text_color
    ).pack(pady=25)

    tk.Label(
        root,
        text=f"Current Score: {score}",
        font=("Arial", 13),
        bg=background_color,
        fg="#58D68D"
    ).pack(pady=5)

    tk.Label(
        root,
        text=f"{number1} {operation} {number2} = ?",
        font=("Arial", 28, "bold"),
        bg=background_color,
        fg=text_color
    ).pack(pady=20)

    # Answer input
    answer_entry = tk.Entry(
        root,
        font=("Arial", 18),
        justify="center",
        width=15
    )
    answer_entry.pack(pady=10)
    answer_entry.focus_set()

    # Submit button
    submit_button = tk.Button(
        root,
        text="Submit Answer",
        font=("Arial", 13),
        bg=button_color,
        fg="white",
        width=18,
        command=checkAnswer
    )
    submit_button.pack(pady=10)

    # Display feedback to the student
    feedback_label = tk.Label(
        root,
        text="",
        font=("Arial", 12),
        bg=background_color,
        fg=text_color
    )
    feedback_label.pack(pady=10)

    # Back button
    tk.Button(
        root,
        text="← Back to Home",
        font=("Arial", 12),
        bg="#566573",
        fg="white",
        command=displayMenu
    ).pack(pady=15)


# Check the student's answer
def checkAnswer():
    global attempts

    if not quiz_active:
        return

    # Prevent multiple submissions while waiting
    if next_question_timer is not None:
        return

    user_answer = answer_entry.get().strip()

    # Check if the answer is a valid number
    try:
        user_answer = int(user_answer)
    except ValueError:
        messagebox.showwarning(
            "Invalid Answer",
            "Please enter a valid whole number."
        )
        return

    attempts += 1

    # Check if the answer is correct
    if user_answer == correct_answer:
        isCorrect(True)
        schedule_next_question()

    else:
        if attempts == 1:
            feedback_label.config(
                text="Incorrect! Try again.",
                fg="#F4D03F"
            )

            answer_entry.delete(0, tk.END)
            answer_entry.focus_set()

        else:
            isCorrect(False)
            schedule_next_question()


# Award points and show feedback
def isCorrect(correct):
    global score

    if correct:
        if attempts == 1:
            score += 10
            feedback_label.config(
                text="Correct! You earned 10 points.",
                fg="#58D68D"
            )
        else:
            score += 5
            feedback_label.config(
                text="Correct! You earned 5 points.",
                fg="#58D68D"
            )
    else:
        feedback_label.config(
            text=f"Incorrect! The correct answer was {correct_answer}.",
            fg="#EC7063"
        )


# Wait briefly before displaying the next question
def schedule_next_question():
    global next_question_timer

    # Stop students from submitting again
    submit_button.config(state="disabled")
    answer_entry.config(state="disabled")

    if question_number >= 10:
        next_question_timer = root.after(1200, displayResults)
    else:
        next_question_timer = root.after(1200, displayProblem)


# Show final results and rank
def displayResults():
    global quiz_active, next_question_timer

    if not quiz_active:
        return

    next_question_timer = None
    quiz_active = False

    # Calculate rank
    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    elif score >= 50:
        rank = "D"
    else:
        rank = "F"

    # Final results popup
    messagebox.showinfo(
        "Quiz Completed!",
        f"You completed all 10 questions!\n\n"
        f"Your Score: {score}/100\n"
        f"Your Rank: {rank}\n\n"
        "Well done!"
    )

    # Ask if the student wants to play again
    play_again = messagebox.askyesno(
        "Play Again",
        "Would you like to play another quiz?"
    )

    if play_again:
        displayMenu()
    else:
        root.destroy()


# Display the home menu when the program starts
displayMenu()

# Keep the application running
root.mainloop()
