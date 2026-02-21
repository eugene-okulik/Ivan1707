def choice_of_operation(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@choice_of_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
result = calc(a, b)
print("Результат:", result)