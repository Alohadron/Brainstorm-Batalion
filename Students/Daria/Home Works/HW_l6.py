FILE_NAME = "contacts.txt"
running = True 
while running:
    print("\n--- Phone Number Menu ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Select an option (1-5)")

if choice == '1':
    name = input("Enter name:")
    phone = input("Enter phone number (digits only): ")
    if phone.digit():
        with open(FILE_NAME, "a") as file:
            file.write(f"{name}|{phone}\n")
        print("Contacts added successfully!")
    else: 
        print("Error: Phone number mustcontain only digits.")
        

