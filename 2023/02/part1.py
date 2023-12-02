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

def is_game_possible(game):
    color_limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    for round in game:
        for draw in round:
            if draw[0] > color_limits[draw[1]]:
                return False
    return True

total = 0

for i, game in enumerate(games):
    if is_game_possible(game):
        total += i + 1

print(total)