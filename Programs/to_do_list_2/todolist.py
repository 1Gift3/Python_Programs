#Actions:
#add - Add a new task to the list
#delete -  delete a task from list 
#list - List all task in the list 


# Something to do with deleting is not clear on this.

def main():
    tasks = []

    while True:
        print("/n ====== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to add:"))

            for i in range(n_tasks):
                task = input("Ener the task:")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice =='2':
            print("/nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")    

        elif choice =='3':
            task_index = int(input("Enter the number to mark as done:")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4': 
            taskToDelete = int(input("Enter the number to delete:"))
            if taskToDelete >=0 and taskToDelete < len(tasks):
                tasks.pop(taskToDelete)
                print(f"Task number {taskToDelete} has been removed.")

            else:
                print(f"Task {taskToDelete} was not found.")            

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")        

if __name__ == "__main__":
    main()