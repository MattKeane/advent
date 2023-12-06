import string

letter_priorities = {}

for (i, letter) in enumerate(string.ascii_letters):
    letter_priorities[letter] = i + 1

def get_common_letter(rucksack):
    first_compartment = rucksack[:int(len(rucksack) / 2)]
    second_compartment = rucksack[int(len(rucksack) / 2):]
    first_contents = {}
    second_contents = {}
    for i in range(len(first_compartment)):
        if second_contents.get(first_compartment[i]):
            return first_compartment[i]
        first_contents[first_compartment[i]] = True
        if first_contents.get(second_compartment[i]):
            return second_compartment[i]
        second_contents[second_compartment[i]] = True

with open('input.txt', 'r') as data:
    rucksacks = data.read().split('\n')
    total = 0
    for rucksack in rucksacks:
        total += letter_priorities[get_common_letter(rucksack)]
    print(total)