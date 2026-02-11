def number_plus_ten(line):
    print(int(line.split()[-1]) + 10)


strings = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for text in strings:
    number_plus_ten(text)
