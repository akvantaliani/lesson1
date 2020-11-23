def get_summ(one, two, delimiter='&'):
    one_str = str(one)
    two_str = str(two)
    return one_str + delimiter + two_str


def format_price(price):
    price_int = int(price)
    return f'Цена: {price_int} руб.'


learn_python = get_summ("Learn", "python")
print(learn_python)
print(learn_python.upper())

price_new_format = format_price(56.24)
print(price_new_format)