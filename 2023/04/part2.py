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
    score = 0
    for num in card[1]:
        if winners.get(num):
            score += 1
    return score

card_copies = [1] * len(cards)
total = 0

for i, card in enumerate(cards):
    total += card_copies[i]
    score = get_card_value(card)
    for j in range(i + 1, i + score + 1):
        card_copies[j] += card_copies[i]

print(total)