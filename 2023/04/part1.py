import re

with open('input.txt', 'r') as file:
    ws_regex = re.compile(r'\s+')
    cards = file.read().split('\n')
    cards = [card.split(':')[1] for card in cards]
    cards = [[[int(num) for num in ws_regex.split(batch.strip())] for batch in card.split('|')] for card in cards]

def get_card_value(card):
    winners = {}
    for num in card[0]:
        winners[num] = True
    total = 0
    for num in card[1]:
        if winners.get(num):
            total += 1
    if total == 0:
        return 0
    return 2 ** (total - 1)

print(sum([get_card_value(card) for card in cards]))