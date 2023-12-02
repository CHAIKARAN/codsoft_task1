#To - Do List
import json
import os
from datetime import datetime

TODO_FILE = "todo.json"

def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}

def save_todo(todo):
    with open(TODO_FILE, "w") as file:
        json.dump(todo, file, indent=2)

def display_tasks(todo):
    print("\n--- To-Do List ---")
    tasks = todo["tasks"]
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['date']}")

def add_task(todo):
    title = input("Enter task title: ")
    date = input("Enter due date (DD-MM-YYYY): ")

    try:
        datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return

    new_task = {"title": title, "date": date}
    todo["tasks"].append(new_task)
    save_todo(todo)
    print("Task added successfully.")

def remove_task(todo):
    display_tasks(todo)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        removed_task = todo["tasks"].pop(index)
        save_todo(todo)
        print(f"Task '{removed_task['title']}' removed successfully.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def print_menu():
    print("\n1. Display tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    todo = load_todo()

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(todo)
        elif choice == "2":
            add_task(todo)
        elif choice == "3":
            remove_task(todo)
        elif choice == "4":
            print("Good bye :). Hope you finish the work on time.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
