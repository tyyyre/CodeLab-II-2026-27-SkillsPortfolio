
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

# Calculate a student's total coursework marks
def calculateCoursework(student):
    return (
        student["course1"] +
        student["course2"] +
        student["course3"]
    )


# Calculate the overall percentage out of 160 marks
def calculatePercentage(student):
    coursework = calculateCoursework(student)
    total = coursework + student["exam"]

    percentage = (total / 160) * 100
    return percentage


# Decide the student's grade
def calculateGrade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# Remove the current screen
def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

# Display all student records
def viewAllStudents():
    clearWindow()

    tk.Label(
        root,
        text="All Student Records",
        font=("Arial", 23, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=20)

    # Create a text area for displaying records
    records_text = tk.Text(
        root,
        width=85,
        height=23,
        font=("Consolas", 10),
        bg=WHITE,
        fg=TEXT_COLOR,
        padx=10,
        pady=10
    )
    records_text.pack(padx=15, pady=10)

    total_percentage = 0

    # Display each student's information
    for student in students:
        coursework = calculateCoursework(student)
        percentage = calculatePercentage(student)
        grade = calculateGrade(percentage)

        total_percentage += percentage

        record = (
            f"Name: {student['name']}\n"
            f"Student Number: {student['code']}\n"
            f"Coursework: {coursework}/60\n"
            f"Exam Mark: {student['exam']}/100\n"
            f"Overall Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}\n"
            "----------------------------------------\n"
        )

        records_text.insert(tk.END, record)

    # Calculate the class average
    if students:
        average = total_percentage / len(students)
    else:
        average = 0

    # Display class summary
    records_text.insert(
        tk.END,
        f"\nTotal Students: {len(students)}\n"
        f"Class Average: {average:.2f}%"
    )

    # Prevent editing the records
    records_text.config(state="disabled")

    # Return to the main menu
    tk.Button(
        root,
        text="Back to Menu",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        command=displayMenu
    ).pack(pady=10)

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
    for index, option in enumerate(menu_options):

        # Connect the first button to View All Students
        if index == 0:
            action = viewAllStudents
        else:
            action = None

        tk.Button(
            root,
            text=option,
            font=("Arial", 12),
            bg=BLUE_COLOR,
            fg=WHITE,
            width=30,
            pady=5,
            command=action
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
