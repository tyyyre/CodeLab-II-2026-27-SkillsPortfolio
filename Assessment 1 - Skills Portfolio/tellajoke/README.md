Exercise 2 – Alexa Tell Me a Joke

Description

This is a joke telling application with interactive interface developed in Python and Tkinter.

The programmed reads jokes from a text file and shows them randomly. The users can interact with Alexa before they see the punchline using response buttons.

The application is themed with Sky Blue and provides a chat-like interface.

 Features

- Welcome screen with a button for “Alexa tell me a Joke”.
37 jokes in external text file.
- Random joke selection.
Each joke has a beginning and an ending.
Interactive response buttons, e.g. "Why?," "What?," "How?."
Punchlines appear once the "Response" button is clicked.
Under the name “Alexa” you will find the messages of Alexa.
- User's messages are shown below the name "hamza".
The sender's names appear in a smaller font, different font.
- Chat-style message bubbles.
The Next Joke button is displayed once the application is running.
Quit button – to end the program.
Handling errors in case the text file is not present.

 Files Used

`main.py` – This is the Python file with the program.

`randomJokes.txt` contains the jokes used by the application.

The joke is written on a line by itself, followed by a question mark.

Example:

```text
Why did the chicken cross the road? To get to the other side.
```

 How to Run

Open `tellajoke` folder in Visual Studio Code.
2. Make sure Python 3 is installed.
3. Make sure `main.py` and `randomJokes.txt` are in the same folder.
4. Run the following command:

bash
python main.py

 How to Use

1. Open the application.
2. tap "Alexa tell me a Joke".
3. Alexa presents a random setup of a joke.
4. Click on the human-response button to show the punch line.
5. Press "Next Joke" to listen to another joke.
Close the application by clicking on the "Quit" button.

 Python Concepts Used

- Functions
- Lists
- Random selection
- File handling
- String manipulation
- Conditional statements
- Event handling
The use of Tkinter labels, buttons and frames
- Exception handling

 How the Joke System Works

This program reads jokes from randomJokes.txt.

It has the question mark to denote the separation between the set-up and the punch line to the joke.

The random module chooses a joke and the setup is first printed out.

As the user clicks the right answer button, the user's response is placed in the chat, and then Alexa's punch line is displayed.

 Conclusion

This exercise was useful for me to learn reading of external text files and displaying the information in a graphical user interface. I also found out how to use functions, random selection and buttons in an interactive application.
