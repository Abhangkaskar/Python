def display_tasks(tasks):
    if not tasks:
        print ("no tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("\nOptions: [1] Add Task [2] View Tasks [3] Remove Task [4] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            idx = int(input("Enter the task number to remover: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
main()