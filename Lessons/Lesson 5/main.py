import os
# note = input("Input your note: ")

# with open("Lessons/Lesson 5/note.txt", 'w') as file:
#     file.write(note)

# with open("Lessons/Lesson 5/note.txt", 'r') as file:
#     print(file.read())

# new_note = input("input your new note: ")

# file = open("Lessons/Lesson 5/note.txt", "a")
# file.write("\n" + new_note)

# with open("Lessons/Lesson 5/note.txt", 'r') as file:
#     print(file.read())

# data = "Hello! MY name is Ion\n"
# with open("Lessons/Lesson 5/note.txt", 'w+') as file:
#     file.seek(0, 2)
#     for i in range(5):
#         file.write(data)

# if os.path.exists("Lessons/Lesson 5/note.txt"):
#     os.remove("Lessons/Lesson 5/note.txt")

import os

while True:
    print("Hello! I am a \'Fast Note\'")
    print("Choose an activity: ")
    print("-- 1 -- Add new note")
    print("-- 2 -- Rewrite note")
    print("-- 3 -- Add note to exits file")
    print("-- 0 -- Remove note")
    print()

    action = int(input("What u gonna do?!!!: "))

    if action == 1:
        print("wHAT DO YOU WANT TO NOTE?")
        note = input("Write the note: ")
        file_path = input("Input file name: ")

        with open(file_path, "w") as file:
            file.write(note)

    elif action == 2:
        exists_file = input("Which file do you want to read? \nfile_name(without .txt): ")
        full_path_ex_file = exists_file + ".txt"

        if os.path.exists(full_path_ex_file):
            with open(full_path_ex_file, "r") as file:
                print(file.read())
        else:
            print("File does not exist")
            continue

    elif action == 3:
        exists_file = input("Which file do you want to add to? \nfile_name(without .txt): ")
        full_path_ex_file = exists_file + ".txt"

        if os.path.exists(full_path_ex_file):
            new_note = input("add new note: ")

            with open(full_path_ex_file, "r+") as file:
                file.seek(0, 2)
                file.write(new_note + "\n")
        else: 
            print(f"file with name - {exists_file} does not exist")
            continue

