# password = (input("Enter your password: "))
# if password == "12345":
#     print("HELLO")

# while(True):
#     if password != "12345":
#         continue
#     if password != "12345":
#             continue
#     if password != "12345":
#             continue
#     # if password != "12345":
#     #         break

# if password == "12345":
#     print("HELLO")

# # numbers = []
# var = input("Enter: ")
# if var == "12345":
#         print("HELLO")
# else:
#       for i in range(3):
#              var != "12345"
#              print("try again")

password = (input("Enter your password: "))
while(True):
    if password != "12345":
        break
    if password == "12345":
        continue 

print("<MENU>")
print("1. top up your bank account  2. withdraw money  3. leave")
option = int(input("Choose an option: "))
match option:
    case "1":
        bills = input("Insert your bills")
        print("Operation was succesfull. Thank you")
    # case "2":
