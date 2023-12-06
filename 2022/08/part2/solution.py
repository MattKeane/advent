with open('input.txt', 'r') as data:
    rows = [[int(tree) for tree in row] for row in data.read().split('\n')]
    view_scores = [[1 for tree in row] for row in rows]
    max_score = 0
    for i, row in enumerate(rows):
        left_view = dict((i, 0) for i in range(10))
        for j, tree in enumerate(row):
            view_scores[i][j] *= left_view[tree]
            for height in range(0, tree + 1):
                left_view[height] = 1
            for height in range(tree + 1, 10):
                left_view[height] += 1 
    for j in range(len(rows[0])):
        top_view = dict((i, 0) for i in range(10))
        for i in range(len(rows)):
            tree = rows[i][j]
            view_scores[i][j] *= top_view[tree]
            for height in range(0, tree + 1):
                top_view[height] = 1
            for height in range(tree + 1, 10):
                top_view[height] += 1
    for i in range(len(rows) - 1, -1, -1):
        right_view = dict((i, 0) for i in range(10))
        for j in range(len(rows) - 1, -1, -1):
            tree = rows [i][j]
            view_scores[i][j] *= right_view[tree]
            for height in range(0, tree + 1):
                right_view[height] = 1
            for height in range(tree + 1, 10):
                right_view[height] += 1
    for j in range(len(rows[0]) - 1, -1, -1):
        bottom_view = dict((i, 0) for i in range(10))
        for i in range(len(rows) -1, -1, -1):
            tree = rows[i][j]
            view_scores[i][j] *= bottom_view[tree]
            if view_scores[i][j] > max_score:
                max_score = view_scores[i][j]
            for height in range(0, tree + 1):
                bottom_view[height] = 1
            for height in range(tree + 1, 10):
                bottom_view[height] += 1
    print(max_score)