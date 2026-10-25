# Default data
message = "Python is fun"

# Task: write message into notes.txt,
# then read the file and print its content

# ADD YOUR CODE HERE
with open("notes.txt", "w") as f:
    f.write(message)
with open("notes.txt", "r") as f:
    print(f.read())