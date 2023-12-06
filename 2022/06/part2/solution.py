from collections import deque
from itertools import islice

def check_if_all_unique(buffer):
    existing = {}
    for letter in buffer:
        if existing.get(letter):
            return False
        existing[letter] = True
    return True

with open('input.txt', 'r') as data:
    datastream = data.read()
    buffer = deque(datastream[:13], maxlen=14)
    for i, letter in enumerate(datastream[13:]):
        buffer.append(letter)
        if check_if_all_unique(buffer):
            print(i + 14)
            break