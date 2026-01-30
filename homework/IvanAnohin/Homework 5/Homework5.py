person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

text = "результат операции: 42"
number = int(text.split(": ")[1])
print(number + 10)

text = "результат операции: 514"
number = int(text.split(": ")[1])
print(number + 10)

text = "результат работы программы: 9"
number = int(text.split(": ")[1])
print(number + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = students[0] + ', ' + students[1] + ', ' + students[2]
subjects_str = subjects[0] + ', ' + subjects[1] + ', ' + subjects[2]

print(f'Students {students_str} study these subjects: {subjects_str}')
