Exercise 3 – Student Manager
Description
This is a Student Manager project written in Python with Tkinter library.

The application enables users to view, search, sort, add and delete a student's academic record along with updating the record.

Student information is kept in a text file and the application automatically assigns total marks, percentages and grades.

The user interface is in the Sky Blue theme.

 Features

 1. View All Student Records

Gets a table of all students, their marks in coursework and exam, their total marks, percentage, and grade.

It also shows the total number of students and the average of the class.

 2. This option displays the Individual Student Record. This will show Individual Student Record.

Searches for a student by student number and displays the student's academic information.

3. Select the Show Highest Scoring Student option. Click on Show Highest Scoring Student.

Identifies and shows the student who has the most points.

 4. Show Lowest Scoring Student

Locates and shows the student who has the least marks.

 5. Sort Student Records

Enables students sorting by total marks ascending or descending.

 6. Add Student Record

Can add a new student including student number, name, coursework marks, exam marks.

Application validates information before saving.

 7. Delete Student Record

Searches and removes a student record if confirmed.

 8. Update Student Record

Enables to search for a student, edit the student information and save the updated information.

 Files Used

`main.py` – The code for the Student Manager application.

This file, called `studentMarks.txt`, contains student academic marks.

The number of students is on the first line of the text file.

The rest of the lines are the following:
StudentNumber,Name,Coursework1,Coursework2,Coursework3,Exam Marking System

| Assessment | Maximum Marks |
| Coursework 1 | 20 |
| Coursework 2 | 20 |
| Coursework 3 | 20 |
| Exam | 100 |
| Total | 160 |

The overall percentage is based on:
Percentage = (Total Marks / 160) × 100
 Grading System

| Percentage | Grade |
| 70% and above | A |
| 60%–69.99% | B |
| 50%–59.99% | C |
| 40%–49.99% | D |
| Below 40% | F |

 How to Run

Use Visual Studio Code to open the studentmanager folder.
2. Make sure Python 3 is installed.
3. Ensure that the main.py and studentMarks.txt are in the same folder.
4. Run the following command:

bash
python main.py

How to Use

1. Open the application.
Choose a one of the eight options on the main menu.
3. Follow instructions on the screen.
Press "Back to Menu" to get back to the main menu.
5. close the app by using the "Quit" button.

 Data Validation

The app validates what the user has typed before it stores the data.

Numbers of students are to be in the form of exactly four digits.
- Duplicate student numbers are not allowed.
Student names are not allowed to be left blank or to include a comma.
Marks for coursework will be in the range 0-20.
- Exam marks must be between 0 and 100.
- Marks must be entered as whole numbers.

 File Handling

When a student application starts up, it begins to load students from studentMarks.txt.

If a student is added, deleted or modified, the application saves the changes to the same text file.

The students' population in the first line is also automatically updated.

 Python Concepts Used

- Functions
- Lists and dictionaries
Read and write files.
- Conditional statements
- Loops
- Sorting
- Lambda functions
- Input validation
- Exception handling
- Tkinter GUI
- Treeview tables

 Conclusion

This exercise provided an understanding of data manipulation using python List and Dictionaries. I also learned how to read and write the text files, how to calculate the percentages, grades, validate user input, and create graphical interface using Tkinter.