# var = input("enter a number: ")

# var_int = int(var) #convert string car to int

# var_int *= 2
# print(var_int)

# var_int += var_int
# print(var_int)

# var_int %= 3 #остаток
# print(var_int)

 
# x = input ("enter a number: ")
# y = input ("enter a 2nd number: ") #input either a number or a letter

# # new_x = int(x)
# # new_y = int(y)
# # x= int(x)
# # y= int(y) #convert boolean to number only, no letters

# equal = x == y

# greater_than = x > y
# less_than = x < y   
# less_than_or_equal = x <= y
# greater_than_or_equal = x >= y

# print("X equal Y ?" , equal, type(equal))
# print("X is greater than Y ?" , greater_than ,type(greater_than))
# print("X is less Than Y?" , less_than_or_equal , type(less_than_or_equal))
# print("X is less than or equal to Y?" , less_than_or_equal , type(less_than_or_equal))
      
guests = ["Misha" , "Mila" , "Dima" , "Nikita"]

names = [] #empty list for names

name_1 = input("Input a name:")
name_2 = input("Input a name:") 
name_3 = input("Input a name:")
name_4 = input("Input a name:")

names.append(name_1) #append to add smth
names.append(name_2)
names.append(name_3)
names.append(name_4)

names_copy = names

names.append("Lora") 
print(names_copy)   
print(names_copy is names)
print(names == guests)
print("1" in names or "Danik" in names) #or shows only if one of the two is true
#and shows only if both are true