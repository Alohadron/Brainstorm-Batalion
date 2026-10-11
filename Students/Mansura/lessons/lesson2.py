# var = input("Enter a number:")
# var_int = int(var)

# var_int *= 2
# print(var_int)

# var_int += var_int
# print(var_int)

# var_int %= 3
# print(var_int)

# x = input(" enter a number:")
# y = input(" enter a second number:")

# equal = x == y
# print(equal, type(equal))

# greater_than = x > y
# print(greater_than, type(greater_than))

# less_than = x < y
# print(less_than)

# less_than_or_equal = x <= y
# print(less_than_or_equal)

# greater_than_or_equal = x >= y
# print(greater_than_or_equal)


guests = ["Liam", "Emma", "Danik", "Olivia"]
names = []

name_1 = input("Input a name:")
name_2 = input("Input a name:")
name_3 = input("Input a name:")
name_4 = input("Input a name:")

names.append(name_1)
names.append(name_2)
names.append(name_3)
names.append(name_4)

names_copy = names

names.append("Lora")

print(names_copy)

print(names_copy is names)

print(names == guests)

print("Masha" in names or "Danik" in names)