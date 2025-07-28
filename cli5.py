# importing the date module to check/analyse due date of task given.
import datetime as dt

# importing datetime to play arithmetic operations btw datetimes.
from datetime import datetime

# importing the json module to stringify and  parsing task as we need to store in file.
import json

# importing the os module to clear the file in path|dir.
import os

date = dt.datetime.today()

# formating date and time to check the due date format and accessing.
dd = date.strftime("%d")
mm = date.strftime("%m")
yyyy = date.strftime("%Y")
formatedDate = f"dd-mm-yyyy : {dd}-{mm}-{yyyy}"

# Task Management template
class Task:

    def __init__(self,filename):

        if(os.path.exists(filename)):

            return
        
        with open(filename,'x') as file:

            print(f"{filename} has created for managing tasks...")

    def addTask(self,filename,name,desc,cate,due,prior):

        print()

        self.name = name

        if(not(self.name)):
            
            print("Providing taskname is compulsory!")
            return

        self.desc = desc

        if(not(self.desc)):
            self.desc=""
        
        self.cate = cate

        if(not(len(self.cate))):
            self.cate=[]

        self.dueDate = due

        if(not(self.dueDate)):
            self.dueDate=""

        self.prior = prior

        if(not(self.prior)):

            print("Note : prior will be set default as ( medium ) if it is empty...")
            self.prior = "medium"

        #task = f"TaskName={self.name},Description={self.desc},Category={self.cate},DueDate={self.dueDate},Prior={self.prior}\n"

        task = dict(taskname=self.name,description=self.desc,category=self.cate,duedate=self.dueDate,prior=self.prior)

        s_json = json.dumps(task)

        if(os.path.exists(filename)):

            print()

            with open(filename,'a') as file:

                file.write(f"{s_json}\n")

            print("Task Added Successfully..!")

        else:

            print("Cannot add tasks : No such file exist... kindly press exit and run to create new instance for managing tasks...")



        #print(formatedDate)

    def displayTasks(self,filename):

        print()

        if(os.path.exists(filename)):

            with open(filename,'r') as file:

                tasks = file.readlines()

                if(tasks):
                    for i,task in enumerate(tasks,start=1):

                        p_json = json.loads(task)
                        
                        print(f"{i}. {p_json}")
                else:
                    print("No tasks to be displayed here...")
        else:

            print("Cannot Display Tasks : No such file exist... kindly press exit and run to create new instance for managing tasks...")

    def displayByCategory(self,filename,category):

        print()

        categories = []

        if(os.path.exists(filename)):

            with open(filename,"r") as file:

                tasks = file.readlines()

                for i,task in enumerate(tasks,start=1):

                    p_json = json.loads(task)

                    if(category in p_json['category']):

                        categories.append(p_json)
                    

            #print(categories)

            if(not(categories)):

                print("No such categories available still.You can add one!")

            else:
                
                print(f"{category} - Categories shown below as you needed,")

                for i,task in enumerate(categories,start=1):

                    print(f"{i}. {task}")
        
        else:

            print("Cannot display tasks by category : No such file exist... kindly press exit and run to create new instance for managing tasks...")
       
    def displayByPriority(self,filename):

        print()

        priority = []

        high = []
        
        medium = []

        low = []

        if(os.path.exists(filename)):

            with open(filename,"r") as file:

                tasks = file.readlines()

                for i,task in enumerate(tasks,start=1):

                    p_json = json.loads(task)
                    # print(p_json)

                    if(p_json['prior'] == "high"):

                        high.append(p_json)

                    elif(p_json['prior'] == 'medium'):

                        medium.append(p_json)

                    elif(p_json['prior'] == 'low'):

                        low.append(p_json)

                    else:

                        print("No priors set here...")

            
            # extends the priority list by concating high,medium,low.

            priority.extend(high)

            priority.extend(medium)

            priority.extend(low)

            for i,task in enumerate(priority,start=1):

                print(f"{i}. {task}")

        else:

            print("Cannot display tasks by priority : No such file exist... kindly press exit and run to create new instance for managing tasks...")

    def updateTask(self,filename,taskname):

        

        if(os.path.exists(filename)):

            update = []

            updated_tasks = []
        
            with open(filename,'r') as file:

                tasks = file.readlines()

                for i,task in enumerate(tasks,start=1):

                    p_json = json.loads(task)

                    if(p_json["taskname"]==taskname):

                        update.append(p_json)

                    
            if(len(update)>1):

                print("You cannot update more than one task at once...")
                    
            elif(len(update)==1):

                try:

                    key = input(f"what do you wanna update in {taskname}? : ").lower()

                    if(key == 'category'):

                        values = []

                        cates = int(input("Enter number of categories? : "))

                        while cates>0:

                            inp = input("Enter category : ")

                            values.append(inp)

                            cates -= 1

                        for s_task in update:

                            s_task[key] = values

                    else:

                        if(key == 'prior'):

                            value = input(f"Enter value for {key} (high,medium,low) : ").lower()

                            if(not(value)):

                                print("Note : if prior value entered empty, it will take default value as 'medium' !")

                                for s_task in update:

                                    s_task[key] = 'medium'

                            else:

                                for s_task in update:

                                    s_task[key] = value

                        else:
                            value = input(f"Enter value for {key} : ")

                            for s_task in update:

                                s_task[key] = value

                    #print(update)
                    updated_tasks = [*update]
                    #print(updated_tasks)

                    try:
                        
                        with open(filename,"r") as file:

                            tasks = file.readlines()

                            for task in tasks:

                                p_json = json.loads(task)

                                if(p_json['taskname'] == update[0]['taskname']):

                                    continue

                                updated_tasks.append(p_json)
                        #print(updated_tasks)

                        with open(filename,"w") as file:

                            for task in updated_tasks:

                                s_json = json.dumps(task)

                                file.write(f"{s_json}\n")

                        print("Task Updated Successfully...")
                        #print(updated_tasks)

                    except Exception as error:

                        print(f"Error Message : {error}")




                except Exception as error:

                    print(f"Error Message : {error}")

            else:

                print("No Updating task available still. You can add one!")   

        else:

            print("Cannot update tasks : No such file exist... kindly press exit and run to create new instance for managing tasks...")     

    def removeTask(self,filename,taskname):

        print()

        remove = []

        other_tasks = []

        if(os.path.exists(filename)):

            try:

                with open(filename,'r') as file:

                    tasks = file.readlines()

                    for task in tasks:

                        p_json = json.loads(task)

                        if(p_json['taskname'] == taskname):

                            remove.append(p_json)

                with open(filename,'r') as file:

                    tasks = file.readlines()

                    for task in tasks:

                        p_json = json.loads(task)

                        if(p_json['taskname']==remove[0]['taskname']):

                            continue

                        other_tasks.append(p_json)

                # remove list will be emptied by clear() method
                remove.clear()

                with open(filename,'w') as file:

                    for task in other_tasks:

                        s_json = json.dumps(task)

                        file.write(f"{s_json}\n")

                print(f"{taskname} is removed successfully...")


            except Exception as error:

                print(f"Error Message : {error}")
        
        else:

            print("Cannot remove tasks : No such file exist... kindly press exit and run to create new instance for managing tasks...")

    def clearTasks(self,filename):

        print()

        # checking if given file exists.

        if(os.path.exists(filename)):

            # remove the file from os (even in system).
            os.remove(filename)

            print("All Tasks cleared successfully...You can Add task to Initialize!")

        else:

            print("No such file exist! kindly press exit and run to create new instance for managing tasks...")





# Operation codes goes here 
print()

print("CONSOLE BASED TASK MANAGEMENT SYSTEM :)")

print()

print("NOTE : To Initialize the Task Management,Instance should be created, here your name could be the instance.")

print()

# Asking for instance | object for initialzing.

instance = input("Enter Your Name : ")

if(instance==""):

    print("Instance cannot be empty..! Kindly Enter your name to Initialize...")

    pass

else:

    instance = Task("Tasks.txt")

    #print("file created !")

    while True:

        print("""
Choose any operations to manage tasks,
                1. Add Task
                2. Display Tasks
                3. Display Tasks by Category
                4. Display Tasks by Priority
                5. Update Task
                6. Clear All Tasks
                7. Remove Task
                8. Exit         
""")
        
        try:

            operation = int(input("Enter Operation: "))

            if(operation==1):

                print()

                print("Initializing the Task...")

                print()

                name = input("Enter Task Name : ").lower()

                desc = input("Enter Description : ").lower()

                cate = []

                try:

                    n_cate = int(input("Number of Categories ? : "))

                    while n_cate>0:

                        c = input("Enter Category : ").lower()

                        n_cate -= 1

                        cate.append(c)

                    

                except Exception as error:

                    print(f"Note : Category is Empty...")

                


                due = input("Enter Due Date (dd-mm-yyyy) : ")

                if(due):

                    d,m,y = due.split('-')

                    if(int(d)>31 or int(d)==0):

                        print(f"Date format is invalid. {d} day is not accepted")

                        continue

                    if(int(m)>12 or int(m)==0):

                        print(f"Invalid Date format, {m} month is cannot exceed 12 months")

                        continue

                    if(len(y)>4 or len(y)<4 or int(y)==0):

                        print(f"Invalid Date format, enter yyyy format properyly")

                        continue

                    if(int(y)<int(yyyy) or int(y)==0):

                        print(f"Invalid Date format, year {y} is past, we cannot accept")

                        continue

                    

                    today = datetime(year=int(yyyy),month=int(mm),day=int(dd))
                    given = datetime(year=int(y),month=int(m),day=int(d))

                    #print(type(today),type(given))
                    
                    # date validation checking.
                    validate = str(given - today)
                    day,time = validate.split(',')
                    check = day.split(" ")
                    #print(check)

                    if(int(check[0])>-1):

                        print("Date format checked properly...")

                    else:

                        continue


                prior = input("Enter Priority (low,medium,high) : ").lower()

                

                instance.addTask("Tasks.txt",name,desc,cate,due,prior)

            elif(operation==2):

                print()

                print("Displaying the Tasks...")

                instance.displayTasks("Tasks.txt")

            elif(operation==3):

                print()

                category = input("Enter Category : ").lower()

                print("Displaying Tasks by Category...")

                instance.displayByCategory("Tasks.txt",category)

            elif(operation==4):

                print()

                print("Displaying Tasks by Priority from high to low...")

                instance.displayByPriority("Tasks.txt")

            elif(operation==5):
                
                print()

                print("Updating Task...")

                print()

                try:

                    taskname = input("Enter taskname to edit: ").lower()

                    if(taskname):

                        instance.updateTask("Tasks.txt",taskname)

                    else:

                        print("Kindly provide taskname...")
                
                except Exception as error:

                    print(f"Error Message : {error}")

            elif(operation==7):
                
                print()

                print("Remove Task has selected...")

                try:

                    print()

                    taskname = input("Enter taskname to delete: ").lower()

                    if(taskname):

                        instance.removeTask("Tasks.txt",taskname)

                    else:

                        print("Kindly provide taskname...")
                
                except Exception as error:

                    print(f"Error Message : {error}")

            elif(operation==6):
                
                print()

                print("Clear All Tasks has selected...")

                instance.clearTasks("Tasks.txt")


            elif(operation==8):

                print()

                print("Operations Exited...To restart Run Again!")

                break

            else:

                print()

                print("Invalid operation selected..Kindly choose given operation..!")

        except Exception as error:

            print()

            print(f"Error Message : {error}")
            
    