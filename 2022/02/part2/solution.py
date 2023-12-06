def score_round(my_shape, opp_shape):
    my_shape_outcomes = {
        'X': {
            'A': 3,
            'B': 1,
            'C': 2,
        },
        'Y': {
            'A': 4,
            'B': 5,
            'C': 6,
        },
        'Z': {
            'A': 8,
            'B': 9,
            'C': 7,
        },
    }
    return my_shape_outcomes[my_shape][opp_shape]

with open('input.txt', 'r') as data:
    rounds = data.read().split('\n')
    total_score = 0
    for round in rounds:
        shapes = round.split(' ')
        total_score += score_round(shapes[1], shapes[0])
    print(total_score)