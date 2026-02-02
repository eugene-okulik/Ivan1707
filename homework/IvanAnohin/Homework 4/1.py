my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 'text', 4, 5],
    'dict': {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять'},
    'set': {1, 2, 3, 4, 'test'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(42)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'дневник'
my_dict['dict'].pop(1)

my_dict['set'].add(42)
my_dict['set'].pop()

print(my_dict)

