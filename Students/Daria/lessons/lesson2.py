# x = input("Enter a number")
# y =input("Enter a second number")

# equal = x == y
# greater_than = x > y
# less_than = x < y
# less_than_or_equal = x <= y
# greater_than_or_equal = x >=y

# print("x equal y?", equal, type(greather_than))
# print("x is greaterthan y?", less_than_or_equal, type(less_than_or_equal))
# print("x is less than y?", less_than, type(less_than))
# print("x is less than or equal to y?", less_than_or_equal, type(less_than_or_equal))

guests = ['Misha', 'Rita', 'Anna', 'Dasha']
names = []

name_1 = input('Input a name: ')
name_2 = input('Input a name: ')
name_3 = input('Input a name: ')
name_4 = input('Input a name: ')

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



