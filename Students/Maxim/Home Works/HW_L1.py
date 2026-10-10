students = ["Masha", "Mila", "Dima", "Nikita"]
students.append("Artem")
new_students = ["Lama", "NikoSlay"]
students.extend(new_students)
students.insert(0, "Yaroslav")
print(students)
students.remove("Dima")
students.pop(6)
students.sort()
print(students)