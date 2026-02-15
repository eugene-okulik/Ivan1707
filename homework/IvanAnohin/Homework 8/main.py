import random

salary = int(input("Введите зарплату: "))

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(1, 10000)
    total = salary + bonus_amount
else:
    total = salary

print(f"{salary}, {bonus} - ${total}")
