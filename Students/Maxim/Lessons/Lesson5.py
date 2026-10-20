# #get a data from console
# message = input('Input your message: ')
# #open connection with file
# file = open('write_1.txt', 'w')
# #write a msg in file
# file.write(message)
# file.close()

# message = input('input your message: ')
# with open('write.txt', 'w') as file:#with open autmatically closes the file
#     file.write(message)
#     # print(file.read()) works if ('write.txt', 'r')



# note = input('Input your note: ')

# with open('Students/Maxim/Lessons/note.txt', 'w') as file:
#     file.write(note)

# with open('Students/Maxim/Lessons/note.txt', 'r') as file:
#     print(file.read())

# new_note = input('Input a new note: ')
# file = open('Students/Maxim/Lessons/note.txt', 'a')
# file.write(new_note)

# with open('Students/Maxim/Lessons/note.txt', 'r') as file:
#     print(file.read())

# import os
# if os.path.exists('Students/Maxim/Lessons/note.txt'):
#     os.remove('Students/Maxim/Lessons/note.txt')

import os

while True:
    print('Hello! I am a \'Fast Note\' ')
    print('Choose an activity')
    print('-- 1 -- add new note')
    print('-- 2 -- rewrite note')
    print('-- 3 -- add note to exist file')
    print('-- 4 -- read note')
    print('-- 5 -- remove note')
    print() 

    action = int(input('What you gonna do?\naction: ')) #\n starts from a new line

    if  action == 1:
        print('What do u want to note?: ')
        note = input('Write a note: ')
        file_name = input('Inpute a file name: ')

        with open (file_name, 'w') as file:
            file.write(note)
    elif action == 2:
        exists_file = input('Which file do u want to rewrite? \nfile_name (without .txt): ')
        full_path_ex_file = exists_file + '.txt'

        if os.path.exists(full_path_ex_file):
            new_note = input('write new note: ')

            with open (full_path_ex_file, 'w+') as file:
                file.write(new_note)
        else:
            print(f"file name - {exists_file} doesn\'t exist")
            continue
    elif action == 3:
        exists_file = input('Where do u want to add note? \nfile_name (without .txt): ')
        full_path_ex_file = exists_file + '.txt'

        if os.path.exists(full_path_ex_file):
            new_note = input('add new note: ')

            with open(full_path_ex_file, 'r+') as file:
                file.seek(0, 2)
                file.write(new_note + '\n')

        else:
            print (f'file wit name - {exists_file} doesn\'t exist')
            continue
    elif action == 4: 
        exists_file = input('Which file do u want to read? \nfile_name (without .txt): ')
        full_path_ex_file = exists_file + '.txt'

        if os.path.exists(full_path_ex_file):
            with open(full_path_ex_file, 'r') as file:
                note = file.read()
            print(f'your note from {exists_file}')
            print('note: ' + note)
        else:
            print(f'file with name - {exists_file} doesn\'t exist')
            continue
    elif action == 5:
        exists_file = input ('Which file do u want to remove? \nfile_name (without .txt): ')
        full_path_ex_file = exists_file + '.txt'

        if os.path.exists(full_path_ex_file):
            os.remove(full_path_ex_file)
        else:
            print(f'file with name - {exists_file} doesn\'t exists')
            continue

    else:
        print('Doesnt\'t exist actione -- choose again')
