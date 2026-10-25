import os
# note = input("Input your note: ")

# with open('Students/Mansura/lessons/note.txt', 'w') as file:
#     file.write(note)

# with open('Students/Mansura/lessons/note.txt', 'r') as file:
#     print(file.read())

# new_note = input('Input a new note: ')

# file = open('Students/Mansura/lessons/note.txt', 'a')
# file.write("\n" + new_note)

# with open('Students/Mansura/lessons/note.txt', 'r+') as file:
#     print(file.read())

# if os.path.exists("Students/Mansura/lessons/note.txt"):
#     os.remove("Students/Mansura/lessons/note.txt")

while True:
    print("Hello I am a \'Fast Note' ")
    print('Choose an activity: ')
    print('--1-- Add new note')
    print('--2-- Rewrite note')
    print ('--3-- Add note to existing file')
    print('--4-- Remoe note')
    print()
    action = int(input('What you gonna do? \naction: '))
    if acton ==1:
        print("What do you want to note?")
        note = input("Write a note: ")
        file_name = input("Input a file name: ")

        with open(file_name, 'w') as file:
         file.write(note)
    elif action == 2:
        exists_file = input("Which file do you want to rewrite \nfile_name (without.txt): ")
        full_path_ex_file = exists_file + '.txt'

    if os.path.exists(full.path.ex.file):
        new_note = input('write new note: ')

        with open (full_path_ex_file, 'w+') as file:
            file.write(new_note)
    else:
        print(f'file with name - {exists_file} doesn\'t exist')
        continue
    elif action == 3:
    exists_file = input("Where do you want to add note? \nfile_name (without .txt): ")
    full_path_ex_file = exists_file + '.txt'

    if os.path.exists(full_path_ex_file):
        new_note = input("add new note:")

        with open(full_path_ex_file, 'r') as file:
            file.seek(0,2)
            file.write(new_note + '\n')
    else:
        print(f'file with name - {exists_file} doesn\'t exist')
        continue 
