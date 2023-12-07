from collections import Counter
from functools import cached_property

class Hand:
    card_values = {
        '2': 0,
        '3': 1,
        '4': 2,
        '5': 3,
        '6': 4,
        '7': 5,
        '8': 6,
        '9': 7,
        'T': 8,
        'J': -1,
        'Q': 10,
        'K': 11,
        'A': 12,
    }

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)

    @cached_property
    def hand_type(self):
        counts = Counter(self.cards)
        most_common = None
        second_most_common = None
        for count in counts.most_common():
            if count[0] == 'J':
                continue
            if not most_common:
                most_common = count
            else:
                second_most_common = count
                break
        else:
            return 6
        if most_common[1] + counts['J'] == 5:
            return 6
        if most_common[1] + counts['J'] == 4:
            return 5
        if most_common[1] + counts['J'] == 3 and second_most_common[1] == 2:
            return 4
        if most_common[1] + counts['J'] == 3:
            return 3
        if most_common[1] + counts['J'] == 2 and second_most_common[1] == 2:
            return 2
        if most_common[1] + counts['J'] == 2:
            return 1
        return 0

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return Hand.card_values[self.cards[i]] > Hand.card_values[other.cards[i]]
        return False

    def __ge__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return Hand.card_values[self.cards[i]] > Hand.card_values[other.cards[i]]
        return True

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return Hand.card_values[self.cards[i]] < Hand.card_values[other.cards[i]]
        return False

    def __le__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return Hand.card_values[self.cards[i]] < Hand.card_values[other.cards[i]]
        return False        

with open('input.txt', 'r') as file:
    hands = [Hand(*line.split(' ')) for line in file.read().splitlines()]

hands.sort()

total_winnings = 0

for i, hand in enumerate(hands):
    total_winnings += hand.bid * (i + 1)

print(total_winnings)