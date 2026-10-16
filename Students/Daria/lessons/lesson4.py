# number = []

# for i in range(10):
#     var = input("Input a nubrer:")
#     var = int(var)
#     number.append(var)

# for num in number:
#     if num % 2 == 0:
#         print(f"{num}: Even")
#     else:
#         print(f"{num}: odd")


while(True):
    word = input("Input your word: ")

    if word.capitalize() == "Finish":
        break
    if word.capitalize().startswith("M"):
        continue 
    for char in word:
        print(char)
