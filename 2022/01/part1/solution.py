with open('input.txt', 'r') as data:
    elves = [elf.split('\n') for elf in data.read().split('\n\n')]
    max_calories = None
    for elf in elves:
        total_calories = 0
        for calorie in elf:
            total_calories += int(calorie)
        if not max_calories or total_calories > max_calories:
            max_calories = total_calories
    print(max_calories)