import json
import os

# To-Do List Manager
# Project 3 - Syntecxhub Python Internship

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    """Load tasks from the JSON file. Return an empty list if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)

        if isinstance(tasks, list):
            # Keep only valid task records
            return [
                task for task in tasks
                if isinstance(task, dict)
                and isinstance(task.get("title"), str)
                and isinstance(task.get("completed"), bool)
            ]

        print("Warning: tasks.json has an invalid format. Starting with an empty list.")
        return []
    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not load saved tasks ({error}). Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to JSON so they remain available after restarting."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Error: Could not save tasks ({error}).")
        return False


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})
    if save_tasks(tasks):
        print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--------------- YOUR TASKS ---------------")
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")
    print("------------------------------------------")


def choose_task_number(tasks, prompt):
    """Ask for a valid task number; return its zero-based index or None."""
    if not tasks:
        print("There are no tasks to select.")
        return None

    try:
        number = int(input(prompt).strip())
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return None

    if not 1 <= number <= len(tasks):
        print(f"Invalid task number. Enter a number from 1 to {len(tasks)}.")
        return None

    return number - 1


def mark_completed(tasks):
    view_tasks(tasks)
    index = choose_task_number(tasks, "Enter task number to mark completed: ")
    if index is None:
        return

    if tasks[index]["completed"]:
        print("This task is already completed.")
        return

    tasks[index]["completed"] = True
    if save_tasks(tasks):
        print("Task marked as completed!")


def mark_pending(tasks):
    view_tasks(tasks)
    index = choose_task_number(tasks, "Enter task number to mark pending: ")
    if index is None:
        return

    if not tasks[index]["completed"]:
        print("This task is already pending.")
        return

    tasks[index]["completed"] = False
    if save_tasks(tasks):
        print("Task marked as pending!")


def delete_task(tasks):
    view_tasks(tasks)
    index = choose_task_number(tasks, "Enter task number to delete: ")
    if index is None:
        return

    removed = tasks.pop(index)
    if save_tasks(tasks):
        print(f"Deleted task: {removed['title']}")


def show_menu():
    print("\n========== TO-DO LIST MANAGER ==========")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Mark task as pending")
    print("5. Delete task")
    print("6. Exit")
    print("========================================")


def main():
    tasks = load_tasks()
    print("Welcome to the To-Do List Manager!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            mark_pending(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Your tasks are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
