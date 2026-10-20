

# msg = input ("Write a message: ")

# with open('write.txt', 'w+') as file:
#     file.write(msg)





# with open('message.txt', 'w') as file:
#     file.write('Maxim\n')
#     file.write('Age 16\n')
#     file.write('Fav language - python\n') #\n starts from a new line

# with open('story.txt','w') as file:
#     file.write('Hi\n')
#     file.write('How are u?\n')
#     file.write('How ur day been?\n')
#     file.write('Did u like the weather?\n')
#     file.write('Have a good day!\n')
# with open('story.txt', 'r') as file:
#     print(file.read())

with open('notes.txt', 'w') as file:
    file.write('Sushi\n')
    file.write('are really\n')
    file.write('tasty\n')
with open('notes.txt','a') as file:
    file.write('and\n')
    file.write('healthy\n')
with open('notes.txt', 'r') as file:
    print(file.read())