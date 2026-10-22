# Show all contacts
elif choice == '3':
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("Phone book is empty.")
            else:
                print("\n--- All Contacts ---")
                for contact in contacts:
                    name, phone = contact.strip().split('|')
                    print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("Phone book is empty.")

