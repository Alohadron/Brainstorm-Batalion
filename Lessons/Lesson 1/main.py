
string_single = 'Hello'
string_double = "Hello"

print(string_single, string_double)

text = "Programming"
slice_1 = text[:6]
slice_2 = text[5:]
slice_3 = text[::-1]

print(f"Original: {text}")
print(f"Slice_1: {slice_1}") 
print(f"Slice_2: {slice_2}")
print(f"Slice_3: {slice_3}")

print(string_single.upper())
print(string_double.lower())
print()

user_input = input("Enter any number: ")

print(f"Data type after input: {type(user_input)}")

number = int(user_input)
print(f"Data type after conversion: {type(number)}")

final_sum = number + 5
print(f"Final sum: {final_sum}")


