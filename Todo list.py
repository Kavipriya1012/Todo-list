import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.readlines()
    return []

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task)

# Main program
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task + "\n")
            save_tasks(tasks)
            print(f"Task '{task}' added.")

        elif choice == "2":
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
            try:
                task_number = int(input("Enter the task number to remove: "))
                removed_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Task '{removed_task.strip()}' removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "3":
            if not tasks:
                print("No tasks available.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
