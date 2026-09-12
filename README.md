<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />
Death Notepad ⏳🗑️
Basic Details
Team Name: Useless Duo
Team Members
Member 1: Nikhil 
Member 2: Arjuna Krishna R
Project Description
Temporary Notepad is a deliberately useless desktop notepad built
with Python and Tkinter. It allows users to type notes, but
automatically deletes the entire note after 2 seconds of inactivity,
making it almost impossible to keep information for long.
The project turns the simple act of taking notes into a funny challenge:
if you stop typing, your note disappears.
The Problem (that doesn't exist)
People are becoming too successful at remembering and saving
information.
Modern users have notes apps that preserve their thoughts, reminders,
ideas, passwords, shopping lists, and important information. This
project solves the completely unnecessary problem of notes lasting too
long.
Ridiculous Problem
> "What if my notes stayed available long enough for me to actually use
> them?"
That sounds terrible. So we fixed it.
The Solution (that nobody asked for)
Temporary Notepad introduces an auto-forget system.
Whenever the user types something, a 2-second timer starts. Every new
keystroke resets the timer. If the user stops typing for 2 seconds and
there is text in the notepad:
The text is detected.
The deletion counter increases.
A random sarcastic message is displayed.
The entire note is permanently removed from the textbox.
Pressing Esc closes the application.
The result is a notepad that successfully prevents productivity.
Technical Details
Technologies/Components Used
For Software:
Language: Python
GUI Framework: Tkinter
Libraries: `random`
Tools: Python interpreter, any Python-compatible code editor or
IDE
For Hardware:
No special hardware is required.
A normal computer or laptop is sufficient.
Implementation
For Software:
Installation
Python 3 is required.
Tkinter is included with most standard Python installations. No external
Python packages are required for this project.
Save the program as:
``` text
temporary\_notepad.py
```
Run
Open a terminal in the folder containing the file and run:
``` bash
python temporary\_notepad.py
```
On some systems, use:
``` bash
python3 temporary\_notepad.py
```
How It Works
The application creates a Tkinter window containing:
A title: TEMPORARY NOTEPAD
A deleted-notes counter
A status/message area
A large text input area
The text box uses the `<KeyRelease>` event to detect typing.
Each time a key is released:
``` text
Typing detected
      ↓
Cancel previous timer
      ↓
Start a new 2-second timer
      ↓
User continues typing?
   ↙          ↘
 Yes           No
  ↓             ↓
Reset timer   Delete note
                ↓
        Increase counter
                ↓
        Show random message
```
Main Program Logic
The `TemporaryNotepad` class controls the application.
The `reset\_timer()` function cancels the previous timer and starts a new
2-second countdown.
The `delete\_text()` function checks whether the textbox contains text.
If text exists, it:
Increases `deleted\_count`
Updates the deletion counter
Selects a random message from the predefined message list
Clears the textbox
The `close\_app()` function destroys the Tkinter window when the user
presses Esc.
Project Documentation
Screenshots
![Screenshot1](temporary_notepad_main_window.png)
Main Temporary Notepad interface showing the title, deletion counter,
message area, and text box.
![Screenshot2](temporary_notepad_typing.png)
The user typing a note before the 2-second inactivity timer expires.
![Screenshot3](temporary_notepad_deleted.png)
The note has disappeared automatically and the deleted-notes counter
has increased.
Workflow
``` text
                Start Application
                       ↓
                Create Tkinter UI
                       ↓
                  User Types
                       ↓
              Key Release Detected
                       ↓
              Reset 2-Second Timer
                       ↓
              User Keeps Typing?
                ↙             ↘
              YES              NO
               ↓                ↓
          Reset Timer       Delete Text
                                ↓
                         Increase Counter
                                ↓
                       Random Funny Message
                                ↓
                           Wait for Input
                                ↓
                         User Types Again
```
Workflow showing how the application detects inactivity and
automatically deletes notes.
Project Demo
Video
Add a short demo video showing:
Opening the Temporary Notepad.
Typing a message.
Stopping for 2 seconds.
Watching the message disappear.
Showing the increased deletion counter.
Pressing Esc to close the application.
Additional Demos
The project can also demonstrate different messages being displayed
after each deletion because the application randomly selects a message
from its predefined collection.
Team Contributions
Project Team: Designed the useless-project concept and user
experience.
Python Development: Implemented the Tkinter interface, timer
logic, text deletion, counter, and keyboard controls.
Testing & Documentation: Tested the 2-second deletion behavior
and prepared the project documentation.
---
Why Is This Project Useless?
Because it does the opposite of what a notepad should do.
A normal notepad says:
> "Write it down. I'll save it."
Temporary Notepad says:
> \*\*"Write it down. I'll delete it."\*\*
Features
⏱️ 2-second automatic deletion
🔄 Timer resets whenever the user types
🗑️ Tracks the number of deleted notes
🎲 Displays random sarcastic messages
⌨️ Supports keyboard-based interaction
🚪 Press Esc to exit
💻 Requires no special hardware
🚫 Provides absolutely no useful long-term note storage
---
Made with ❤️ and absolutely no respect for your notes at TinkerHub
Useless Projects.
 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



