import re


def health(name):
    health_ch = re.finditer(health_expr, name)
    health = 0
    for ch in health_ch:
        health += ord(ch.group(0))
    return health


def damage(name):
    damages = re.finditer(damage_expr, name)
    current_damage = 0
    for damage in damages:
        current_damage += float(damage.group())
    operators_expr = r'[/\*]'
    operators = re.findall(operators_expr, name)
    for operator in operators:
        if operator == '*':
            current_damage *= 2
        elif operator == '/':
            current_damage /= 2
    return current_damage


data = input()
demons_expr = r'\s*,\s*'
health_expr = r'[^\d\*\/\+\.\-]'
damage_expr = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demons_list = re.split(demons_expr, data)

for demon in sorted(demons_list):
    health_points = health(demon)
    damage_points = damage(demon)
    print(f'{demon} - {health_points} health, {damage_points:.2f} damage')
