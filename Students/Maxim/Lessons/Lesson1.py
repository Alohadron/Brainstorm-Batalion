string_single = "Hello"
string_double = "World"

print(string_single, string_double)


text = "Programming"
slice_1 = text[0:5]
slice_2 = text[5:]
slice_3 = text[: : -1]


print(f"Original: {text}")  
print(f"Slice_1: {slice_1}")
print(f"Slice_2: {slice_2}")
print(f"Slice_3: {slice_3}")
print()



print(string_single.upper())
print(string_double.lower())
print()

user_input = input("Введите какое-нибудь число (например, 10): ")

print(f"Тип данных после input(): {type(user_input)}")  

number = int(user_input)
print(f"Тип данных после int(): {type(number)}")

final_sum = number + 5
print(f"Результат сложения вашего числа с пятеркой ({number} + 5): {final_sum}")

print("Hello")