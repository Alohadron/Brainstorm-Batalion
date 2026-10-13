students = ['Masha', 'Mila', 'Dima', 'Nikita']
students.append('Artem')
new_students = ['Lola', 'Nastya']
students.extend(new_students)
students.insert(0,'Yaroslav')
students.remove('Dima')
students.pop()
students.sort()
print(students)