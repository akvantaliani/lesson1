a = None
b = 0
print(a is None)
print(b is not None)
print(type(a))
print(type(b))
a = input('Введите ваше имя: ')
user_name_input = a.capitalize()
print(f'Привет, {user_name_input}')
d = '{:{prec}} = {:{prec}}'.format('Gibberish', 32.7182, prec='.3')
print(d)