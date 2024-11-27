TasksList = []

def load_task():
    with open("tasks.txt", "r") as file:
        lines = file.readline()
        task_data = lines.strip().split('|')
        print(task_data)
        TasksList.append((task_data[0],task_data[1]))
        TasksList.append({"description": task_data[0], "status": task_data[1]})
        
def addtask():

    task_description = input("\nEnter the task: ")
    formatted_task = f"{task_description}|incomplete\n"
    with open("tasks.txt" , "a") as file:
        file.write(formatted_task)

    TasksList.append((task_description , "incomplete"))

    print(f"\nTask {task_description} added successfully.\n")
    
def viewtask():
    if not TasksList:
        print("list is empty")
    
    for index, task in enumerate(TasksList):
        print(f"{index +1}. {task}")

def markascompleted():
    print()

    while True:
        
        task_number = int(input("enter the task number you want to be as completed: "))
        
    
        if task_number >=1 and task_number <= len(TasksList):
         break

        else:
         print(f"Invalid task number! choose between 1 and {len(TasksList)}")

    index = task_number -1

    TasksList[index] += " - Completed"

    print()

    print(f"Task {task_number} ('{TasksList[index]}') has been marked as completed")

def removal():

    while True:
     print()
     choice = int(input("Enter the number: "))
     

     if choice >= 1 and choice <= len(TasksList):
         break
     else:
         print(f"you entered wrong, enter between 1 - {len(TasksList)} ")

    print()
    index = choice -1

    TasksList.pop(index)

    print("Entry is removed successfully")

    print()

def Menu_Selection():
    
    print("\n1. Add a Task")
    print("2. View Tasks")
    print("3. Mark as completed")
    print("4. Remove a task")
    print("5. Exit \n")
   
    

    GetNumber = int(input("Enter your number: "))
    print()

    if GetNumber == 1:
        print("add a task")
        addtask()

    elif GetNumber == 2:
        print("tasks")
        viewtask()

    elif GetNumber == 3:
        print("Mark as completed")
        markascompleted()

    elif GetNumber == 4:
        print("Task Removal")
        removal()

    elif GetNumber == 5:
        print("Exiting")
    else:
        print("Entered invalid")

    return GetNumber

def Main():
    
    load_task()

    while True:
        
        Choice = Menu_Selection()

        if  Choice == 5:
            
            exitcommand = input("are you sure to exit? (yes/no)").lower()
            print()
            
            if exitcommand in ['yes', 'y']:
                print("GoodBye")
                exit()

            elif exitcommand in ['no','n']:
                print("returning to menu...")
                print()
                

            else:
                print("please enter in correct way")


Main() 
