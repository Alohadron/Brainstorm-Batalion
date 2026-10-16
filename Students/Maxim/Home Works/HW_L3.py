# age = int(input("Enter your age:"))
# if(age < 13):
#     print("child")
# elif(age < 18):
#     print("teenager")
# elif(age < 64):
#     print("adult")
# else:
#     print("elderly")

number_1 = int(input("Enter 1st number:")) 
operation = (input("Enter operation:")) 
number_2 = int(input("Enter 2nd number:"))
match operation:
    case "+":
      print("result:", number_1 + number_2)
    case "-":
        print("result:" , number_1 - number_2)
    case "*":
        print("result:" , number_1 * number_2)
    case "/" if number_2 == 0:
        print("invalid number")
    case "/":
        print("reslut:" , number_1 / number_2)
    case _:
           print("incorrect operation")
