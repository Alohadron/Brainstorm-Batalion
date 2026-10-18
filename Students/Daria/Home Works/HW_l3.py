age = input("enter your age:")

if int(age) < 13:
    print("Child")
elif 13 <= int(age) < 18:
    print("Teenager")
elif 18 <= int(age) < 64:
    print("Adult")
elif 64<= int(age) < 100:
    print("Senior")
