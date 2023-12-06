with open('input.txt', 'r') as f:
    pairs = [[eval(packet) for packet in pair.split('\n')] for pair in f.read().split('\n\n')]

def compare(left, right):
    ltype, rtype = type(left), type(right)
    if ltype is int and rtype is int:
        if left < right:
            return 'right'
        if right < left:
            return 'wrong'
        if left == right:
            return False
    if ltype is list and rtype is list:
        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return 'right'
            if i >= len(right):
                return 'wrong'
            compared_values = compare(left[i], right[i])
            if compared_values:
                return compared_values
        return False
    if ltype is int:
        return compare([left], right)
    else:
        return compare(left, [right])

total = 0

for i, pair in enumerate(pairs):
    if compare(pair[0], pair[1]) == 'right':
        total += i + 1

print(total)