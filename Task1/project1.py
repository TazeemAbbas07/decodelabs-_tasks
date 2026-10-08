my_tasks=[]

while True:

    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Exit")

    choice=input("Enter the choice: ")

    if choice=="1":

        task=input("Enter task: ")
        my_tasks.append(task)
        print("Task Added Successfully")

    elif choice=="2":

        print("Your Tasks: ")
        if not my_tasks:
            print("No Tasks ")
        else:
            for number,task in enumerate(my_tasks,start=1):
                print(f"{number} : {task} ")

    elif choice=="3":

        print("Exited")
        break

    else:

        print("Invalid Choice, Please Try Again")
        