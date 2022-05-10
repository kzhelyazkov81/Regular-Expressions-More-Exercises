import re

total_income = 0
expression = '\%(?P<name>[A-Z][a-z]+)\%[^\$\%\|\.]*<(?P<product>\w+)>[^\$\%\|\.]*\|(?P<count>[0-9]+)\|[^\$\%\|\.1-9]*(?P<price>([0]|[1-9][0-9]*)[\.]?\d*)\$'
while True:
    data = input()
    if data == 'end of shift':
        break
    match = re.match(expression, data)
    if match:
        name = match['name']
        product = match['product']
        count = int(match['count'])
        price = float(match['price'])
        total_price = count * price
        total_income += total_price
        print(f'{name}: {product} - {total_price:.2f}')
print(f'Total income: {total_income:.2f}')
