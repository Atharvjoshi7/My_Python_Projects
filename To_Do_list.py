
tasks = []

while True:
    print("1. add Task")
    print("2. view Tasks")
    print("3. remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.\n")
    elif choice == '2':
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    elif choice == '3':
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                tasks.pop(num - 1)
                print("Task removed.\n")
            except (ValueError, IndexError):
                print("Invalid number.\n")
        else:
            print("No tasks to remove.\n")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")

