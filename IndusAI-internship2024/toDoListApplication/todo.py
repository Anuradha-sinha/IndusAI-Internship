tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTasks are :")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Deleted task: {removed_task}")
    else:
        print("Invalid task number.")

def main():
   
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_index = int(input("\nEnter the task number to delete: ")) - 1
                delete_task(task_index)
                view_tasks()
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do List Manager. \nThanks you")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
