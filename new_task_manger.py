from datetime import datetime
import os
os.chdir(r"C:\Users\RTX\Music\progect_pythone")
masege="""
1.add task to a list
2.mark task at compleate
3.view task
4.Quit
"""
with open("task_file.txt") as f:
    tasks=f.readlines()


def main():

        while True:
            print(masege)
            choise=input("enter the number of your choise: ")

            if choise=='1':
                add_task()

            elif choise=='2':
                mark_task()

            elif choise=='3':
                view_task()

            elif choise=='4':
                break         
            else:
                print("invalid choise,please enter number between 1 t 4")

tasks_not_complete=[]

def add_task():
    task=input("enter your task please: ")
    date=input("enter date of task: (yyyy-dd-mm)")
    try:
        invstgate_from_date=date.split("-")
        invstgate_from_date=[int(num)for num in invstgate_from_date]
        try:
            date2=datetime.strptime(date,"%Y-%m-%d")
            task_info={"name":task,"completed":False,"date":date2}
            tasks.append(task_info)
            print("task added to list")
        except:
            print("invalide date formate,please enter date in (yyyy-mm-dd) formte")  
    except:
        print("please enter date numbers not string")


def mark_task():
        if len(tasks)==0: print("-"*20),print("no task avilable to mark"); return

        tasks_not_complete=[task1 for task1 in tasks if task1["completed"]==False ]

        for i,task in enumerate(tasks_not_complete):
                print(f"{i+1}.{task['name']}")

        try:
            number_task=int(input("please enter number of task to completed: "))
            if number_task < 0 or number_task< len(tasks_not_complete):
                print("invalid number")
                return 
            tasks_not_complete[number_task-1]["completed"]=True
            print("task comleted succssfilly")
            
        except ValueError:
            print("please enter number not string ")

def view_task():
        for i,task in enumerate(tasks):
            status="✔️"if task["completed"]==True else"❌"
            print(f"{i+1}. {task['name']} ({task['date']}) {status}")

            
            
if __name__=="main"            
    main()
