def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()
targets = {5, 200, 1000, 100000}

for i in range(1, max(targets) + 1):
    num = next(gen)
    if i in targets:
        print(f"{i}-е число Фибоначчи: {num}")
