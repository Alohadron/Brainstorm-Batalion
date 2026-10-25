FILE_NAME = "contacts.txt"
running = True
while running:
    print("\n--- Phone Book Menu ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Select an option 1-5")

    if choice == "1":
        name = input("Enter a name: ")
        phone = input("Enter phone number: ")
        if phone.isdigit():
            with open(FILE_NAME, "a") as file:
                file.write(f"{name} {phone}\n")
            print("Contact added successfully")
        else:
            print("Error. Number must contain digits only")

    if choice == "2":
        search_name = input("Enter a name: ")
        found = False
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                     name, phone = line.strip().split("|")
                     if search_name in name:
                        print(f"Found: {name} - {phone}")
                        found = True
            if not found:
              print("Contact not found")
        except FileNotFoundError:
            print("Phone book is empty")

    if choice == "3":
        try:
            with open(FILE_NAME, "r") as file:
                contacts = file.readlines()
                if not contacts:
                    print("Phone book is empty")
                else:
                    print("\n--- All contacts ---")
                    for contact in contacts:
                        name, phone = contact.strip().split("|")
                        print(f"Name: {name}, Phone: {phone}")
        except FileNotFoundError:
            print("Phone book is empty")