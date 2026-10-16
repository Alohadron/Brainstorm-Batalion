# numbers = []

# for i in range(10):
#     var = input('Input a random number: ')
#     var = int(var)
#     numbers.append(var)

# for num in numbers:
#     if num % 2 == 0:
#         print(f'{num}: even')
#     else:
#         print(f'{num}: odd')

# names = []

# while(True):
#     name = input("Input your name: ")

#     if name == "Ivan":
#         break
#     else:
#         pass

#     names.append(name)

# for name in names:
#     print(name)

while(True):
    word = input("Input your word: ")

    if word.capitalize() == "Finish":
      break

    if word.capitalize().startswith("M"):
       continue

    for char in word:
       print(char)