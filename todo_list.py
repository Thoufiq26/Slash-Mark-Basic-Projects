# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    """Displays the list of tasks with their status."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")
    print("\n")

# Function to add a task to the to-do list
def add_task(task_name):
    """Adds a new task to the list."""
    if task_name.strip() == "":
        print("Task name cannot be empty. Please enter a valid task.")
    else:
        task = {"task": task_name, "completed": False}
        tasks.append(task)
        print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_number):
    """Marks the specified task as completed."""
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    """Removes the specified task from the list."""
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        display_tasks()
        try:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")