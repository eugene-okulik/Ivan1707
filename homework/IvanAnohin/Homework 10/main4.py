PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

names = [line.split()[0] for line in PRICE_LIST .splitlines()]
price = [line.split()[1][:-1] for line in PRICE_LIST.splitlines()]

new_list = dict(zip(names, price))

print(new_list)
