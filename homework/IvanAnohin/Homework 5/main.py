person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

text = "результат операции: 42"
number = int(text[text.index(':') + 2:])
print(number + 10)

text = "результат операции: 514"
number = int(text[text.index(':') + 2:])
print(number + 10)

text = "результат работы программы: 9"
number = int(text[text.index(':') + 2:])
print(number + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
subjects = ', '.join(subjects)
print('Students', students, 'study these subjects:', 'subjects', subjects)
