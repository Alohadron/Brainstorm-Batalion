correct_password = "1234"
balance = 50000

attempts = 3
access = False 
while attempts > 0:
    password = input("Enter a password:")
    if password == correct_password:
        print("Correct password")
        access = True 
        break
    else:
        print("Incorrect password")
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left")
        else:
            print("No more attempts")
            break

while access:
    print(f"your balance: {balance}")
    print("Enter 1 for withdraw")
    print("Enter 2 for deposit")
    print("Enter 0 for exit")
    user_input = input("Enter your value:")
    if user_input == "0":
        print("Thank you")
        break
    elif user_input == "1":
        amount = int(input("Enter an amount to withdraw:"))
        if balance >= amount:
            balance -= amount
            print(f"You succesfull withdrew: {amount}")
        else:
            print("Insufficint funds")
    elif user_input == "2":
        amount = int(input("Enter an amount to deposit:"))
        if amount > 0:
            balance += amount
            print(f"You succesfull deposited: {amount}")
        else:
            print("Error: Deposit amount must be positive")
    else:
        print("Invalid option")
        break