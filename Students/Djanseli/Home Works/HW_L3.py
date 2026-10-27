def add_task(tasks: list) -> None:
  # Prompt the user for a task and add it to the list
 task = input("Введите задачу: ")
 tasks.append(task)

def show_tasks(tasks: list) ->None:
  # Display the list of tasks with their index numbers
  for i in range(len(tasks)):
    print(i + 1, "-", tasks[i])

def remove_task(tasks: list) -> None:
      #Prompt for a task number and remove if from the list
      index = int(input("Введите номер задачи для удаления: "))
      tasks.pop(index - 1)

def main ():
   tasks = []
   while True:
      #1. Print menu
      print("1. Показать задачу")
      print("2. Добавить задачу")
      print("3. Удалить задачу")
      print("4. Выйти")

      # 2. Get user choice 
      choice = input("Выберите пуект: ")

      #3. Call the appropriate function 
      if choice == "1":
         show_tasks(tasks)
      elif choice == "2":
       add_task(tasks)
      elif choice == "3":
         remove_task(tasks)
      elif choice == "4":
         break  # Replace with exit logic

main()

