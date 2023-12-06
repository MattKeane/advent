def check_pair(pair):
    assignments = [[int(section) for section in assignment.split('-')] for assignment in pair.split(',')]
    if assignments[0][0] <= assignments[1][1] and assignments [0][1] >= assignments[1][0]:
        return True
    if assignments[1][0] <= assignments[0][1] and assignments [1][1] >= assignments [0][0]:
        return True
    return False

with open('input.txt', 'r') as data:
    pairs = data.read().split('\n')
    total = 0
    for pair in pairs:
        if check_pair(pair):
            total += 1
    print(total)