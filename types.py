a = 2
b = 0.5
print(a + b)

name = 'Александр'
name_hello = f'Привет, {name}!'
print(name_hello)

v = input('Введите число от 1 до 10: ')
print(int(v)+10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

print(float('1'))
print(int('2.5')) #exception: ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1))
print(bool(''))
print(bool(0))