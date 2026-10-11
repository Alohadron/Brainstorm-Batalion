students = ["Masha" , "Mila" , "Dima" , "Nikita"]

students.append("Artem")

new_students = ["Sasha" , "Vlad"]
students.extend (new_students) 

students.insert(0, "Yaroslav")  
students.remove("Dima")
students.pop(6)

students.sort()
print(students)
