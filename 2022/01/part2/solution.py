with open('input.txt', 'r') as data:
    elves = [elf.split('\n') for elf in data.read().split('\n\n')]
    first = 0
    second = 0
    third = 0
    for elf in elves:
        total_calories = 0
        for calorie in elf:
            total_calories += int(calorie)
        if total_calories > first:
            third = second
            second = first
            first = total_calories
        elif total_calories > second:
            third = second
            second = total_calories
        elif total_calories > third:
            third = total_calories
    print(first + second + third)