authenticated_users = []
user_name = input("Enter your user name please:")
login = input("Enter your login pleae:")
#if user_name in authenticated_users:
#    print("Welcome back!")
if login == "1234":
    print("Welcome back!")
    authenticated_users.append(user_name)

else:
    print("NO ACCESS")

code = int(input("Enter a number:"))

selected = []
match code:
    case 1:
        print("Pizza, 110 lei")
        selected.append(1)
    case 2:
        print("burger, 80 lei")
        selected.append(2)
    case 3:
        print("Coke, 35 lei")
        selected.append(3)
    case 4:
        print("Bread sticks, 15 lei")
        selected.append(4)
    case 5:
        print("Milkshake, 45 lei")
        selected.append(5)
    case 6:
        print("Soup, 90 lei")
        selected.append(6)
    case _:
        print("Invalid Code")