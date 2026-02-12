secret_number = 4

user_guess = int(input('Угадай цифру от 0 до 9: '))

while user_guess != secret_number:
    print('Попробуй снова!')
    user_guess = int(input('Угадай цифру от 0 до 9: '))

print('Поздравляю! Вы угадали!')
