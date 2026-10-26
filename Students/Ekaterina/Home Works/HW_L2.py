with open(FILE_NAME, "w") as file:
    for line in lines:
        if '|' in line:
            name, phone = line.strip().split('|')
            if name.lower() != name_to_delete:
                file.write(line)
            else:
                found = True

if found:
    print("Contact deleted.")
else:
    print("Contact not found.")