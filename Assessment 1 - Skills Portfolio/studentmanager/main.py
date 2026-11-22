
import tkinter as tk
from tkinter import messagebox
import os

# Sky Blue theme colours
BG_COLOR = "#F0F5FF"
BLUE_COLOR = "#3478D4"
TEXT_COLOR = "#253A59"
WHITE = "#FFFFFF"

# Create the main application window
root = tk.Tk()
root.title("Student Manager")
root.geometry("750x600")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# List to store student records
students = []


# Function to load student records from the text file
def loadStudents():
    students_list = []

    # Find the folder where main.py is saved
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "studentMarks.txt")

    try:
        # Open the student marks file
        with open(file_path, "r", encoding="utf-8") as file:

            # First line contains the number of students
            student_count = int(file.readline().strip())

            # Read the remaining student records
            for line in file:
                line = line.strip()

                if line:
                    data = line.split(",")

                    # Store student information in a dictionary
                    student = {
                        "code": data[0],
                        "name": data[1],
                        "course1": int(data[2]),
                        "course2": int(data[3]),
                        "course3": int(data[4]),
                        "exam": int(data[5])
                    }

                    students_list.append(student)

    except FileNotFoundError:
        messagebox.showerror(
            "File Error",
            "studentMarks.txt could not be found."
        )

    return students_list


# Function to display the main menu
def displayMenu():

    # Application heading
    tk.Label(
        root,
        text="Student Manager",
        font=("Arial", 26, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=30)

    tk.Label(
        root,
        text="Student Records Management System",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=BLUE_COLOR
    ).pack(pady=5)

    # Main menu options
    menu_options = [
        "View All Student Records",
        "View Individual Student Record",
        "Show Highest Scoring Student",
        "Show Lowest Scoring Student",
        "Sort Student Records",
        "Add Student Record",
        "Delete Student Record",
        "Update Student Record"
    ]

    # Create buttons for each menu option
    for option in menu_options:
        tk.Button(
            root,
            text=option,
            font=("Arial", 12),
            bg=BLUE_COLOR,
            fg=WHITE,
            width=30,
            pady=5
        ).pack(pady=5)

    # Quit button
    tk.Button(
        root,
        text="Quit",
        font=("Arial", 12),
        bg="#E1E9F4",
        fg=TEXT_COLOR,
        width=30,
        command=root.destroy
    ).pack(pady=15)


# Load student records
students = loadStudents()

# Display the main menu
displayMenu()

# Keep the application running
root.mainloop()
