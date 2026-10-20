correct_password = "1234"
balance = 50000

attempts = 3
password_granted = False
while attempts > 0:
    password = input("Enter a password:")
    if password == correct_password:
        print("Correct password")
        password_granted = True 
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password")
            break
while password_granted:
    print(f"your balance: {balance}")
    print("Enter 0 for entrance")
    user_input = input("Enter your value:")
    if user_input == "0":
        print("Thank you")
        break
    if amount > balance: 
        print("Error")
        continue
    if amount < 0:
        print("Error")
        continue
    balance -= amount 
    print(f"Succesfull: {amount}")
    

