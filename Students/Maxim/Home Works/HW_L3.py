# age = int(input("Enter your age:"))
# if(age < 13):
#     print("child")
# elif(age < 18):
#     print("teenager")
# elif(age < 64):
#     print("adult")
# else:
#     print("elderly")

# number_1 = int(input("Enter 1st number:")) 
# operation = (input("Enter operation:")) 
# number_2 = int(input("Enter 2nd number:"))
# match operation:
#     case "+":
#       print("result:", number_1 + number_2)
#     case "-":
#         print("result:" , number_1 - number_2)
#     case "*":
#         print("result:" , number_1 * number_2)
#     case "/" if number_2 == 0:
#         print("invalid number")
#     case "/":
#         print("reslut:" , number_1 / number_2)
#     case _:
#            print("incorrect operation")

door = int(input("Choose a door 1,2 or 3: "))

match door:
    case 1:
        print("You've chosen the red door!")
        print("A dragon was behind the door")
        choice = int(input("1 - Fight , 2 - Run: "))
        if choice == 1:
            print("You've defeated the dragon")
        else:
            print("You've escaped the dragon")
    case 2:
        print("You've chosen the blue door")
        print("There is a treasure chest!")
        number = int(input("Choose a number to open it!: "))
        if number == 7:
            print("You found the treasures!")
        else:
            print("The chest is closed")
    case 3:
        print("You've chosen the green door")
        print("You've met a wizard!")
        age = int(input("Whats your age?: "))
        if age <12:
            print("Your too young for the quest!")
        elif age <=17:
            print("The wizard gave you a magic shield!")
        else:
            print("The wizard gave you a magic sword!")
    case _:
        print("There is no such door")