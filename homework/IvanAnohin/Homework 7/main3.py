def number_plus_ten(text):
    print(int(text.split()[-1]) + 10)

strings = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for text in strings:
    number_plus_ten(text)
