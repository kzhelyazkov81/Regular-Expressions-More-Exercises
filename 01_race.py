import re

participants_expression = r'\w+'
name_expression = r'[A-Za-z]'
meters_expression = r'[0-9]'

data = input()
participants = re.findall(participants_expression, data)
race = {key: 0 for key in participants}
while True:
    data = input()
    if data == 'end of race':
        break
    name_letters = re.findall(name_expression, data)
    meters = re.findall(meters_expression, data)
    participant = ''.join(name_letters)
    distance = sum(map(int, meters))
    if participant in race.keys():
        race[participant] += distance

top_racers = sorted(race.items(), key=lambda item: item[1], reverse=True)
print(f'1st place: {top_racers[0][0]}\n2nd place: {top_racers[1][0]}\n3rd place: {top_racers[2][0]}')
