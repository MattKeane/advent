import string

letter_priorities = {}

for (i, letter) in enumerate(string.ascii_letters):
    letter_priorities[letter] = i + 1

def get_common_letter(rucksack1, rucksack2, rucksack3):
    first_contents = {}
    for letter in rucksack1:
        first_contents[letter] = True
    first_and_second_contents = {}
    for letter in rucksack2:
        if first_contents.get(letter):
            first_and_second_contents[letter] = True
    for letter in rucksack3:
        if first_and_second_contents.get(letter):
            return letter

with open('input.txt', 'r') as data:
    rucksacks = data.read().split('\n')
    total = 0
    for i in range(0, len(rucksacks), 3):
        total += letter_priorities[get_common_letter(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2])]
    print(total)