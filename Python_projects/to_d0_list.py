#functions to collect basic operations for the to-do-list.

#function to add tasks.
# List to store tasks
tasks = []
marked_tasks = []
# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

# Function to display all tasks
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):  # Start numbering from 1
            print(f'{idx}. {task}')
    else:
        print("No tasks in your list!")

     
#function to add completed tasks to the list.
def complete_task(task_to_mark):
    global tasks
    if task_to_mark in tasks:
        global marked_tasks
        marked_tasks.append(task_to_mark)
        tasks.remove(task_to_mark)
        print(f"Task ({task_to_mark}) completed.")
    else:
        print("This task does not exist. Have you created it before?")
     

# def edit_tasks(task):
#     if tasks:
#         return tasks.append(task)
# Infinite loop to keep the program running until user exits
while True:
    print("\nOptions: 1. Add Task  2. Remove Task  3. View Tasks  4. Exit 5. Completed Tasks 6. Edit Tasks")
    # try:
    # Ask user for their choice
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    
    elif choice == '4':
        print("Exiting program. Have a productive day!")
        break
    elif choice == '5':
     task_to_mark =   input("Add completed tasks: ")
     complete_task(task_to_mark)
    elif choice == '6':
        print(view_tasks())
        edited_task = input("Which task do you want to edit: ")  
        # if edited_task == "":

    else:
        print("Invalid choice! Please select a valid option.")

    print("Completed Tasks:", marked_tasks)