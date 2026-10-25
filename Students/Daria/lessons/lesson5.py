# note = input("Input your note")

# with open("Students/Daria/Lessons/note.txt", "w") as file:
#     file.write(note)
# with open("Students/Daria/Lessons/note.txt",) as file:
#     print(file.read())


# new_note = input('Input new note')

# file = open("Students/Daria/Lessons/note.txt", "a")

# file.write(new_note)

# with open("Students/Daria/Lessons/note.txt", "r") as file:
#     print(file.read())
    
# import os 

# if os.path.exists('write.txt'):
#     os.remove('write.txt')

import os
while True:
    print('Hello! I am \'Fast Note\'')
    print('Choose an activity')
    print('-- 1 -- Add new note')
    print('-- 2 -- Rewrite note')
    print('-- 3 -- Add new note toexist file')
    print('-- 4 -- Remove note')
    action = int(input("What u gonna do?\naction:"))
if action == 1
    print('What do u want to note?')
    note = input('Write a note:')
    file_name = input('Input a file name:')

    with open(file_name, "w") as file:
        file.write(note)
elif action == 2:
    exists_file = input("Which file do you want to rewrite? \nfile_name (without.txt):")
    full_path_ex_file = exists_file + 'txt'

    if os.path.exists(full_path_ex_file):
        new_note = input()
    


