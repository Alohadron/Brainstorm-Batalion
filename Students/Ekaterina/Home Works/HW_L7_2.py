# Search contact
elif choice == '2':
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            # Iterate through file lines to find matches
            for line in file:
                name, phone = line.strip().split('|')
                if search_name in name.lower():
                    print(f"Found: {name} - {phone}")
                    found = True
            if not found:
                print("Contact not found.")
    except FileNotFoundError:
        print("Phone book is empty.")
