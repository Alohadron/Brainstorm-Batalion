# numbers = []
# for i in range(10):
#     var = input("Enter a number: ")
#     var = int(var)
#     numbers.append(var)

# for num in numbers:
#     if num % 2 == 0: #shows if the number is even and has no (остаток)
#         print(f"{num}: even")
#     else:
#         print(f"{num}: odd") #even - четное odd - нечетное

       

# names = []
# #Start an infinite loop
# while(True):
#     name = input("Input a name: ")
#     #check if the entered name is "ivan"
#     if name == "Ivan":
#     #immideately terminate the while loop
#         break     
#     else:
#         #do nothing
#         pass
#     #if the name is not ivan add it to the names list
#     names.append(name)
    
#     #iterate through each name in the names list (cycle)
#     for name in names:
#        #print the current name
#        print(name)


while(True):
    word = input('Input your word: ')
    if word.capitalize() == "Finish":
        break

    if word.capitalize().startswith("M"):
        continue
    for char in word:
        print(char)
