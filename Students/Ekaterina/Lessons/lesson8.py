# authorized_user = ["user_123", "mihaiOLLD", "CIRRA", "MILLA"]

# find_name = input("Enter your username: ")

# def authorized(name):
#     for i in authorized_user:
#         if name == i:
#             print("Hello! Nice to see you {name}")
#             break
#         else:
#             print('Sorry! I dont know you')

# authorize(find_name)

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "ERROR! You cannot divide by 0"
    return a / b
