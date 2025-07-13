tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f'"{task}" added to the list.')

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        print(f"{idx}. {task['task']} - {status}")
    print("")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f'Task {task_num} marked as done.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye! Your tasks are safe with Eva 💖")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
