with open('input.txt', 'r') as data:
    rows = [[int(tree) for tree in row] for row in data.read().split('\n')]
    visible = {}
    right_max = {}
    left_max = {}
    top_max = {}
    bottom_max = {}
    visible_count = 0
    for i, row in enumerate(rows):
        for j, tree in enumerate(row):
            if tree > left_max.get(i, -1):
                visible[(j, i)] = True
                left_max[i] = tree
            if tree > top_max.get(j, -1):
                visible[(j, i)] = True
                top_max[j] = tree
    for i in range(len(rows) - 1, 0, -1):
        row = rows[i]
        for j in range(len(row) - 1, 0, -1):
            tree = row[j]
            if tree > right_max.get(i, -1):
                visible[(j, i)] = True
                right_max[i] = tree
            if tree > bottom_max.get(j, -1):
                visible[(j, i)] = True
                bottom_max[j] = tree
    print(len(visible.items()))