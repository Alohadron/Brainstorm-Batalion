# auth_user = ['us1', 'us2', 'us3', 'us4']

# find_name = input('Enter ur user name: ')

# def authorize(name):
#     for i in auth_user:
#         if name == i:
#             print(f'Hello {name}!')
#             break
#         else:
#             print('Sorry idk who is it')
#             break
# #call the method
# authorize(find_name)#put the variable from 'input'

    #function (name/parameter)
# def addition(a, b):
#     return a + b   #return gives a result and continues the programm
# def subtraction(a, b):
#     return a - b
# def multiplication(a, b):
#     return a * b
# def division(a, b):
#     if b == 0:
#         return "Error:cant devide by 0"
#     return a / b

# print(addition(8, 9))
# print(subtraction(67, 2)) 
# print(multiplication(5, 9))
# print(division(8, 2.9)) 
import time 
tasks = []
def add_task(tasks: lists) -> None:#None returns nothing 
    task = input('Name the task')
    tasks.append(task) 
    print("Task added")

def show_task(tasks: lists) -> None:
    for task in tasks:
        print(f'The task is {task} and its index is {tasks.index(task)}\n')
        
def remove_task(tasks: list) -> None:
    task_index = int(input("Enter the task index: "))
    tasks.remove(tasks[task_index])

def main():
    pass
while True:
     #1 add 2 show 3 del task
    print("options")
    print("1 add")
    print("2 show") 
    print("3 remove")
    print("0 to leave")
    option = int(input("choose: "))
    match option:
        case 1:
            add_task(tasks) #add our previous function and the list
            time.sleep(2)
        case 2:
            show_task(tasks) #add function "show_tasks"
            time.sleep(5)
        case 3:
            remove_task(tasks)
            time.sleep(2)
        case 0:
            print("Goodbye!")
            break
