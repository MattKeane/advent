rows = []

with open('sample.txt', 'r') as file:
    for line in file.read().splitlines():
        row, nums = line.split(' ')
        nums = [int(num) for num in nums.split(',')]
        rows.append((row, nums))

def get_arrangements(line, groups):
    total = 0
    group = groups[0]
    if len(groups) == 0:
        i = 0
        while i < len(line) - group + 1:
            if line[i] == '#' or line[i] == '?':
                if i > 0 and line[i - 1] == '#':
                    i += 1
                    continue
                for j in range(group):
                    should_break = False
                    try:
                        if line[i + j] != '#' and line[i + j] != '?':
                            i = i + j
                            should_break = True
                    except IndexError:
                        i = i + j
                        should_break = True
                    if should_break:
                        break
                else:
                    try:
                        if line[i + group] != '#':
                            total += 1
                    except IndexError:
                        total += 1
            i += 1
    else:
        i = 0
        while i < len(line) - group + 1:
            if line[i] == '#' or line[i] == '?':
                if i > 0 and line[i - 1] == '#':
                    i += 1
                    continue
                for j in range(group):
                    should_break = False
                    try:
                        if line[i + j] != '#' and line[i + j] != '?':
                            i = i + j
                            should_break = True
                    except IndexError:
                        i = i + j
                        should_break = True
                    if should_break:
                        break
                else:
                    try:
                        if line[i + group] != '#':
                            total += get_arrangements(line[i + 1:], groups[1:])
                    except IndexError:
                        pass
            i += 1    
    return total

for row in rows:
    print(get_arrangements(row[0], row[1]))