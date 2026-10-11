guests = ['Alice', 'Bob', 'Charlie', 'David']
names =[]

name_1 = input('Enter a name: ')
name_2 = input('Enter a name: ')
name_3 = input('Enter a name:')
name_4 = input('enter a name: ')

names.append(name_1)
names.append(name_2)
names.append(name_3)
names.append(name_4)

names_copy = names

names.append('Lora')

print(names_copy)
print(names_copy is names)
print(names == guests)

print('Masha' in names or 'Danik' in names)