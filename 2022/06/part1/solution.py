from collections import deque
from itertools import islice

def check_if_all_unique(buffer):
    for i, letter in enumerate(islice(buffer, 3)):
        if letter in islice(buffer, i + 1, None):
            return False
    return True

with open('input.txt', 'r') as data:
    datastream = data.read()
    buffer = deque(datastream[:3], maxlen=4)
    for i, letter in enumerate(datastream[3:]):
        buffer.append(letter)
        if check_if_all_unique(buffer):
            print(i + 4)
            break