# To-Do List Manager — Python Project 3

## Project overview
A menu-driven command-line application for managing everyday tasks. Tasks are saved in `tasks.json` so they remain available after the program is closed and reopened.

## Features
- Add a task
- View all tasks and their status
- Mark a task completed
- Mark a task pending again
- Delete a task
- Save/load tasks using JSON
- Handle invalid menu choices, invalid task numbers, empty task names, malformed JSON, and file errors

## Requirements
- Python 3.9 or newer recommended
- Visual Studio Code (optional, but convenient)
- No third-party packages are required

## Run in VS Code
1. Extract the ZIP file.
2. Open the extracted `ToDoListManager` folder in VS Code using **File → Open Folder**.
3. Open `todo_manager.py`.
4. Choose **Terminal → New Terminal**.
5. Run one of these commands:
   - Windows: `py todo_manager.py`
   - Or: `python todo_manager.py`
   - macOS/Linux: `python3 todo_manager.py`

## How to use
Choose a menu number:
1. Add task
2. View tasks
3. Mark task completed
4. Mark task pending
5. Delete task
6. Exit

The `tasks.json` file is created automatically the first time you add a task. Keep it in the same project folder as `todo_manager.py`.

## Test checklist
- Add a task and view it.
- Mark it completed and confirm its status changes.
- Mark it pending again.
- Try an invalid menu choice such as `9`.
- Enter letters instead of a task number when prompted.
- Add a task, exit, reopen the program, and confirm the task remains saved.
- Delete a task and verify it no longer appears.

## Project explanation
- `while` loop: keeps the menu running until Exit is selected.
- `if/elif/else`: handles the selected menu option.
- Functions: separate tasks into manageable operations.
- `json`: stores task data in a structured format.
- `try/except`: handles file and invalid-number errors.
- `os.path`: locates `tasks.json` beside the Python file.

## Submission reminder
Check your internship instructions for the official submission form, file naming rules, deadline, and whether screenshots or a ZIP are required. Do not submit until you have run and tested the project on your computer.
