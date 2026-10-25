# authorized_user = ["user_1234", "bonnie1blue", "kenedy45", "Milla"]

# find_name = input("Enter your username: ")

# def authorize(name):
#     for i in authorized_user:
#         if name == i:
#             print(f"Hello. Nice to see you {name}")
#             break
#         else:
#             print("Sorry. Username not authorized")

# authorize(find_name)

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error. You cant devide by 0"
    else:
        return a / b