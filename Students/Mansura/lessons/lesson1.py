string_single = 'Hello'
string_double = "world"

print (string_single, string_double)

text = "Programming"
slice_1 = text[0:5]
slice_2 = text[5:]
slice_3 = text[::-1]

print(f"Original:{text}")
print(f"Slice_1: {slice_1}")
print(f"Slice_2: {slice_2}")
print(f"Slice_3: {slice_3}")

print(string_single.upper())
print(string_double.lower())
print()

user_input = input ("any number:")

print(f"LOL: {type(user_input)}")

number = int(user_input)
print(f"56: {type(number)}")

final_sum = number +5
print(f"Result of your equation with five ({number}+5): {final_sum}")