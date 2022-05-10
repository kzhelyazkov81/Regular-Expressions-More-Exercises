import re


def encrypt_message(data):
    decrypt_number = 0
    for ch in data:
        if ch.lower() in 'star':
            decrypt_number += 1
    decrypted_message = ''
    for ch in data:
        new_ch = chr(ord(ch) - decrypt_number)
        decrypted_message += new_ch
    return decrypted_message


def substract_planet(encrypted_data):
    expression = r'[^@!:>-]*@(?P<name>[A-Z][a-z]*)[^@!:>-]*:([0-9]+)[^@!:>-]*!(?P<attack>[A]|[D])![^@!:>-]*->([0-9]+)[^@!:>-]*'
    match = re.match(expression, encrypted_data)
    if match is not None:
        planet_name = match['name']
        attack_type = match['attack']
        return planet_name, attack_type
    return None

quantity = int(input())
attacked_planets = []
destroyed_planets = []

for i in range(quantity):
    message = input()
    planet_info = substract_planet(encrypt_message(message))
    if planet_info is not None:
        attack_type = planet_info[1]
        planet = planet_info[0]
        if attack_type == 'A':
            attacked_planets.append(planet)
        elif attack_type == 'D':
            destroyed_planets.append(planet)


print(f'Attacked planets: {len(attacked_planets)}')
if len(attacked_planets) > 0:
    for planet in sorted(attacked_planets):
        print(f'-> {planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
if len(destroyed_planets) > 0:
    for planet in sorted(destroyed_planets):
        print(f'-> {planet}')
