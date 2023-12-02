with open('input.txt', 'r') as data:
    games = []
    for line in [line.split(':')[1] for line in data.read().split('\n')]:
        game = []
        for round in line.split(';'):
            parsed_round = []
            for draw in round.split(','):
                parsed_draw = draw.strip().split(' ')
                parsed_round.append((int(parsed_draw[0]), parsed_draw[1]))
            game.append(parsed_round)
        games.append(game)

def get_cube_minimums(game):
    minimums = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for round in game:
        for draw in round:
            if draw[0] > minimums[draw[1]]:
                minimums[draw[1]] = draw[0]

    return minimums

def get_power(cubes):
    power = 1
    for _, amount in cubes.items():
        power *= amount
    return power

total = sum([get_power(get_cube_minimums(game)) for game in games])

print(total)