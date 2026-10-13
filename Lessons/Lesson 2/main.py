# x = input("Enter a number: ")
# y = input("Eneter a second number: ")

# equal = x == y
# greater_than = x > y
# less_than = x < y
# less_than_or_equal = x <= y
# greater_than_or_equal = x >= y

# print("\nX equal Y ?", equal, type(equal))
# print("X  is greater than Y ?", greater_than, type(greater_than))
# print("X is less than Y ?", less_than, type(less_than))
# print("X is less than or equal to Y ?", less_than_or_equal, type(less_than_or_equal))
# print("X is greater than or equal to Y ?", greater_than_or_equal, type(greater_than_or_equal))

guests = ["John", "Mary", "Peter", "Jane"]
names = []

name_1 = input("Enter a name: ")
name_2 = input("Enter a name: ")
name_3 = input("Enter a name: ")
name_4 = input("Enter a name: ")

names.append(name_1)
names.append(name_2)
names.append(name_3)
names.append(name_4)

names_copy = names 

names.append('Lora')

print(names_copy)
print(names_copy is names)
print(names == guests)

print('Masha' in names and 'Danik' in names)

print("")