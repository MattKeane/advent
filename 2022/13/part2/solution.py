from functools import cmp_to_key

def compare(left, right):
    ltype, rtype = type(left), type(right)
    if ltype is int and rtype is int:
        if left < right:
            return -1
        if right < left:
            return 1
        if left == right:
            return False
    if ltype is list and rtype is list:
        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return -1
            if i >= len(right):
                return 1
            compared_values = compare(left[i], right[i])
            if compared_values:
                return compared_values
        return False
    if ltype is int:
        return compare([left], right)
    else:
        return compare(left, [right])



with open('input.txt', 'r') as f:
    packets = ([eval(packet) for packet in f.read().split('\n') if len(packet) > 0])

divider_1 = [[2]]
divider_2 = [[6]]
packets.extend([divider_1, divider_2])

packets.sort(key=cmp_to_key(compare))

decoder_key = 1
for i, packet in enumerate(packets):
    if packet is divider_1 or packet is divider_2:
        decoder_key *= i + 1

print(decoder_key)