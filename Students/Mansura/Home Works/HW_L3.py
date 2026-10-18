# age = (int(input("Enter your age please:")))

# if age < 13:
#     print("A child")
# elif 13 <= age <= 17:
#     print("A Teenager")
# elif 18 <= age <= 64:
#     print("An Adult")
# else:
#     print("A Senior")


# number_1 = int(input("Enter the first number:"))
# operation = (input("Choose your operation:"))
# number_2 = int(input("Enter the second number:"))
# match operation:
#     case "+":
#         print("result:" , number_1 + number_2)
#     case "-":
#         print("result:", number_1 - number_2)
#     case "*":
#         print("result:", number_1 * number_2)
#     case "/" if number_2 == 0:
#         print("Cant devide by 0")
#     case "/":
#         print("result:", number_1 / number_2)
#     case _: print("Nonexistent operation")



door =(input("Pick a door: red  blue  green: "))
match door:
    case "red":
        print("There is a dragon! What will you do?")
        choice = int(input("1- Fight  2- Run:"))
        if choice ==1:
         print("You have defeated the dragon!")
        else:
         print("You have managed to escape the dragon.")
    case "blue":
        print("You see a treasure chest.")
        number = int(input("Enter a secret number to open it: "))
        if number == 7:
         print("You have found the treasure!")
        else:
         print("The chest is locked.")
    case "green":
        print("Whats your age?")
        age = int(input("Enter your age: "))
        if age <= 12:
         print("Sorcerer: You are too young for this mission im afraid.")
        elif age<= 17:
         print("The sorcerer gives you a magic shield")
        else:
         print("The sorcerer gives you a magic sword")
    case _:
        print("This door does not exist")