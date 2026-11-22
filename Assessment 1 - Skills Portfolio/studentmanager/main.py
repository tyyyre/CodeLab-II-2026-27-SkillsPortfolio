
import tkinter as tk
from tkinter import messagebox, ttk
import os

# Sky Blue theme colours
BG_COLOR = "#A1495F"
BLUE_COLOR = "#000000"
DARK_COLOR = "#112421"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#000000"

# Create the main application window
root = tk.Tk()
root.title("Student Manager")
root.geometry("950x650")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# List used to store student records
students = []

# Find the student marks file
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "studentMarks.txt")


# Load students from the text file
def loadStudents():
    students_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            # The first line contains the number of students
            student_count = int(file.readline().strip())

            # Read the remaining student records
            for line in file:
                line = line.strip()

                if line:
                    data = line.split(",")

                    student = {
                        "code": data[0],
                        "name": data[1],
                        "course1": int(data[2]),
                        "course2": int(data[3]),
                        "course3": int(data[4]),
                        "exam": int(data[5])
                    }

                    students_list.append(student)

        if student_count != len(students_list):
            messagebox.showwarning(
                "Student Count",
                "The student count in the file does not match the records."
            )

    except FileNotFoundError:
        messagebox.showerror(
            "File Error",
            "studentMarks.txt could not be found."
        )

    except (ValueError, IndexError):
        messagebox.showerror(
            "File Error",
            "The student marks file contains invalid data."
        )

    return students_list


# Save student records back to the text file
def saveStudents():
    try:
        with open(file_path, "w", encoding="utf-8") as file:

            # Save the number of students first
            file.write(str(len(students)) + "\n")

            # Save each student's information
            for student in students:
                line = (
                    f"{student['code']},"
                    f"{student['name']},"
                    f"{student['course1']},"
                    f"{student['course2']},"
                    f"{student['course3']},"
                    f"{student['exam']}\n"
                )

                file.write(line)

        return True

    except OSError:
        messagebox.showerror(
            "Save Error",
            "Student records could not be saved."
        )
        return False


# Calculate total coursework marks out of 60
def calculateCoursework(student):
    return (
        student["course1"] +
        student["course2"] +
        student["course3"]
    )


# Calculate total marks out of 160
def calculateTotal(student):
    return calculateCoursework(student) + student["exam"]


# Calculate the student's overall percentage
def calculatePercentage(student):
    return (calculateTotal(student) / 160) * 100


# Calculate the student's grade
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


# Remove widgets from the current screen
def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()


# Create a heading for each screen
def showHeading(title):
    tk.Label(
        root,
        text=title,
        font=("Arial", 24, "bold"),
        bg=BG_COLOR,
        fg=DARK_COLOR
    ).pack(pady=20)


# Create a button to return to the main menu
def backButton():
    tk.Button(
        root,
        text="Back to Menu",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=displayMenu
    ).pack(pady=15)


# Format a student's information
def formatStudent(student):
    coursework = calculateCoursework(student)
    total = calculateTotal(student)
    percentage = calculatePercentage(student)
    grade = calculateGrade(percentage)

    return (
        f"Name: {student['name']}\n"
        f"Student Number: {student['code']}\n"
        f"Coursework: {coursework}/60\n"
        f"Exam Mark: {student['exam']}/100\n"
        f"Total Marks: {total}/160\n"
        f"Overall Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}"
    )


# Create a table to display student records
def createStudentTable(student_list):
    columns = (
        "code", "name", "coursework",
        "exam", "total", "percentage", "grade"
    )

    table = ttk.Treeview(
        root,
        columns=columns,
        show="headings",
        height=15
    )

    # Table headings
    headings = [
        "Student No.", "Student Name", "Coursework",
        "Exam", "Total", "Percentage", "Grade"
    ]

    widths = [100, 180, 110, 80, 80, 110, 70]

    for column, heading, width in zip(columns, headings, widths):
        table.heading(column, text=heading)
        table.column(column, width=width, anchor="center")

    # Insert student records into the table
    for student in student_list:
        table.insert(
            "",
            tk.END,
            values=(
                student["code"],
                student["name"],
                f"{calculateCoursework(student)}/60",
                f"{student['exam']}/100",
                f"{calculateTotal(student)}/160",
                f"{calculatePercentage(student):.2f}%",
                calculateGrade(calculatePercentage(student))
            )
        )

    table.pack(pady=15, padx=20)
    return table


# 1. View all student records
def viewAllStudents():
    clearWindow()
    showHeading("All Student Records")

    createStudentTable(students)

    # Calculate the class average
    if students:
        average = sum(
            calculatePercentage(student) for student in students
        ) / len(students)
    else:
        average = 0

    tk.Label(
        root,
        text=(
            f"Total Students: {len(students)}"
            f"       Class Average: {average:.2f}%"
        ),
        font=("Arial", 14, "bold"),
        bg=BG_COLOR,
        fg=DARK_COLOR
    ).pack(pady=10)

    backButton()


# 2. View an individual student record
def viewIndividualStudent():
    clearWindow()
    showHeading("View Individual Student")

    tk.Label(
        root,
        text="Enter Student Number:",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=DARK_COLOR
    ).pack(pady=10)

    student_entry = tk.Entry(
        root,
        font=("Arial", 14),
        justify="center"
    )
    student_entry.pack(pady=10)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=DARK_COLOR,
        justify="left"
    )
    result_label.pack(pady=20)

    # Search for the student
    def searchStudent():
        student_number = student_entry.get().strip()

        for student in students:
            if student["code"] == student_number:
                result_label.config(text=formatStudent(student))
                return

        result_label.config(text="Student not found.")

    tk.Button(
        root,
        text="Search",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=searchStudent
    ).pack(pady=10)

    backButton()


# 3 and 4. Show highest or lowest scoring student
def showExtremeStudent(highest=True):
    clearWindow()

    if not students:
        messagebox.showwarning(
            "No Students",
            "There are no student records."
        )
        displayMenu()
        return

    if highest:
        selected = max(students, key=calculateTotal)
        showHeading("Highest Scoring Student")
    else:
        selected = min(students, key=calculateTotal)
        showHeading("Lowest Scoring Student")

    tk.Label(
        root,
        text=formatStudent(selected),
        font=("Arial", 15),
        bg=BG_COLOR,
        fg=DARK_COLOR,
        justify="left"
    ).pack(pady=35)

    backButton()


# 5. Sort student records
def sortStudents():
    clearWindow()
    showHeading("Sort Student Records")

    tk.Label(
        root,
        text="Sort students by their overall total marks:",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=DARK_COLOR
    ).pack(pady=10)

    # Sort from lowest to highest
    def ascending():
        sorted_students = sorted(
            students,
            key=calculateTotal
        )
        showSortedStudents(sorted_students, "Ascending")

    # Sort from highest to lowest
    def descending():
        sorted_students = sorted(
            students,
            key=calculateTotal,
            reverse=True
        )
        showSortedStudents(sorted_students, "Descending")

    tk.Button(
        root,
        text="Ascending",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=ascending
    ).pack(pady=10)

    tk.Button(
        root,
        text="Descending",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=descending
    ).pack(pady=10)

    backButton()


# Display sorted student records
def showSortedStudents(sorted_students, order):
    clearWindow()
    showHeading(f"Students Sorted - {order}")

    createStudentTable(sorted_students)
    backButton()


# Validate student information entered by the user
def validateStudent(code, name, course1, course2, course3, exam,
                    original_code=None):

    # Check student number
    if not code.isdigit() or len(code) != 4:
        messagebox.showerror(
            "Invalid Student Number",
            "Student number must contain exactly 4 digits."
        )
        return None

    # Check for duplicate student numbers
    for student in students:
        if student["code"] == code and code != original_code:
            messagebox.showerror(
                "Duplicate Student",
                "This student number already exists."
            )
            return None

    # Check student name
    if not name.strip() or "," in name:
        messagebox.showerror(
            "Invalid Name",
            "Enter a valid name without commas."
        )
        return None

    # Check marks are whole numbers
    try:
        mark1 = int(course1)
        mark2 = int(course2)
        mark3 = int(course3)
        exam_mark = int(exam)
    except ValueError:
        messagebox.showerror(
            "Invalid Marks",
            "All marks must be whole numbers."
        )
        return None

    # Check the allowed marks
    if not all(0 <= mark <= 20 for mark in [mark1, mark2, mark3]):
        messagebox.showerror(
            "Invalid Coursework",
            "Each coursework mark must be between 0 and 20."
        )
        return None

    if not 0 <= exam_mark <= 100:
        messagebox.showerror(
            "Invalid Exam Mark",
            "Exam mark must be between 0 and 100."
        )
        return None

    return {
        "code": code,
        "name": name.strip(),
        "course1": mark1,
        "course2": mark2,
        "course3": mark3,
        "exam": exam_mark
    }


# Create entry boxes for student information
def createStudentForm(existing_student=None):
    entries = {}

    fields = [
        ("Student Number", "code"),
        ("Student Name", "name"),
        ("Coursework 1 (0-20)", "course1"),
        ("Coursework 2 (0-20)", "course2"),
        ("Coursework 3 (0-20)", "course3"),
        ("Exam Mark (0-100)", "exam")
    ]

    for label_text, field_name in fields:
        tk.Label(
            root,
            text=label_text,
            font=("Arial", 11),
            bg=BG_COLOR,
            fg=DARK_COLOR
        ).pack(pady=(6, 2))

        entry = tk.Entry(
            root,
            font=("Arial", 12),
            justify="center",
            width=30
        )
        entry.pack(pady=2)

        # Fill in existing values when updating
        if existing_student:
            entry.insert(0, str(existing_student[field_name]))

        entries[field_name] = entry

    return entries


# 6. Add a student record
def addStudent():
    clearWindow()
    showHeading("Add Student Record")

    entries = createStudentForm()

    # Save the new student
    def saveNewStudent():
        new_student = validateStudent(
            entries["code"].get().strip(),
            entries["name"].get().strip(),
            entries["course1"].get().strip(),
            entries["course2"].get().strip(),
            entries["course3"].get().strip(),
            entries["exam"].get().strip()
        )

        if new_student:
            students.append(new_student)

            if saveStudents():
                messagebox.showinfo(
                    "Success",
                    "Student added successfully!"
                )
                displayMenu()
            else:
                students.remove(new_student)

    tk.Button(
        root,
        text="Save Student",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=saveNewStudent
    ).pack(pady=12)

    backButton()


# Find a student using their student number
def findStudent(code):
    for student in students:
        if student["code"] == code:
            return student

    return None


# 7. Delete a student record
def deleteStudent():
    clearWindow()
    showHeading("Delete Student Record")

    tk.Label(
        root,
        text="Enter the Student Number to delete:",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=DARK_COLOR
    ).pack(pady=15)

    student_entry = tk.Entry(
        root,
        font=("Arial", 14),
        justify="center"
    )
    student_entry.pack(pady=10)

    # Delete the selected student
    def confirmDelete():
        code = student_entry.get().strip()
        student = findStudent(code)

        if student is None:
            messagebox.showerror(
                "Not Found",
                "Student not found."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete {student['name']}?"
        )

        if confirm:
            index = students.index(student)
            students.pop(index)

            if saveStudents():
                messagebox.showinfo(
                    "Success",
                    "Student deleted successfully!"
                )
                displayMenu()
            else:
                students.insert(index, student)

    tk.Button(
        root,
        text="Delete Student",
        font=("Arial", 12),
        bg="#C0392B",
        fg=WHITE,
        width=20,
        command=confirmDelete
    ).pack(pady=15)

    backButton()


# 8. Update a student record
def updateStudent():
    clearWindow()
    showHeading("Update Student Record")

    tk.Label(
        root,
        text="Enter the Student Number to update:",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=DARK_COLOR
    ).pack(pady=15)

    student_entry = tk.Entry(
        root,
        font=("Arial", 14),
        justify="center"
    )
    student_entry.pack(pady=10)

    # Search for the student to update
    def searchForUpdate():
        code = student_entry.get().strip()
        student = findStudent(code)

        if student is None:
            messagebox.showerror(
                "Not Found",
                "Student not found."
            )
            return

        showUpdateForm(student)

    tk.Button(
        root,
        text="Find Student",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=searchForUpdate
    ).pack(pady=15)

    backButton()


# Display the form for updating student information
def showUpdateForm(student):
    clearWindow()
    showHeading("Edit Student Information")

    original_code = student["code"]

    # Fill the form with the current student information
    entries = createStudentForm(student)

    # Save updated information
    def saveUpdate():
        updated_student = validateStudent(
            entries["code"].get().strip(),
            entries["name"].get().strip(),
            entries["course1"].get().strip(),
            entries["course2"].get().strip(),
            entries["course3"].get().strip(),
            entries["exam"].get().strip(),
            original_code
        )

        if updated_student:
            old_student = student.copy()
            student.update(updated_student)

            if saveStudents():
                messagebox.showinfo(
                    "Success",
                    "Student updated successfully!"
                )
                displayMenu()
            else:
                student.update(old_student)

    tk.Button(
        root,
        text="Save Changes",
        font=("Arial", 12),
        bg=BLUE_COLOR,
        fg=WHITE,
        width=20,
        command=saveUpdate
    ).pack(pady=12)

    backButton()


# Display the main menu
def displayMenu():
    clearWindow()

    showHeading("Student Manager")

    tk.Label(
        root,
        text="Student Records Management System",
        font=("Arial", 13),
        bg=BG_COLOR,
        fg=BLUE_COLOR
    ).pack(pady=5)

    # Menu buttons and their functions
    menu_options = [
        ("1. View All Student Records", viewAllStudents),
        ("2. View Individual Student Record", viewIndividualStudent),
        ("3. Show Highest Scoring Student",
         lambda: showExtremeStudent(True)),
        ("4. Show Lowest Scoring Student",
         lambda: showExtremeStudent(False)),
        ("5. Sort Student Records", sortStudents),
        ("6. Add Student Record", addStudent),
        ("7. Delete Student Record", deleteStudent),
        ("8. Update Student Record", updateStudent)
    ]

    # Create all eight menu buttons
    for text, action in menu_options:
        tk.Button(
            root,
            text=text,
            font=("Arial", 12),
            bg=BLUE_COLOR,
            fg=WHITE,
            width=35,
            pady=5,
            command=action
        ).pack(pady=6)

    # Quit button
    tk.Button(
        root,
        text="Quit",
        font=("Arial", 12),
        bg="#E1E9F4",
        fg=DARK_COLOR,
        width=35,
        command=root.destroy
    ).pack(pady=12)


# Load student records when the application starts
students = loadStudents()

# Display the main menu
displayMenu()

# Keep the application running
root.mainloop()
