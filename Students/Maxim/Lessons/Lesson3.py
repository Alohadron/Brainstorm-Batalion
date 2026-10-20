# auth_user = []

# login = input("Enter your login: ")
# password = input("Enter your password: ")

# if(login == "123" and password == "123"):
#     auth_user.append(f"user with login: {login} is authorized")
#     print("You are authorized. Welcome!")
# else:
#     print("Incorrect login or password. Please try again.")





from unittest import case


Selected = int(input("Enter your choice: "))

Selected = []

match Selected:
    case "1":
        Selected.append("You have selected option 1")
    case "2":
        Selected.append("You have selected option 2")
    case "3":
        Selected.append("You have selected option 3")
print(Selected)