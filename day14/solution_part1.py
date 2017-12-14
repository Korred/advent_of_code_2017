from collections import Counter
import sys
sys.path.append('../')

from day10.solution_part2 import knot_hash

data = "stpzcrnm"


def create_disc(data, size):
    disc = []
    for i in range(size):
        kh = knot_hash(data + f'-{i}')
        line = []
        for c in kh:
            b = bin(int(c, 16))[2:]
            line.extend(list(map(int, list('0'*(4-len(b)) + b))))

        disc.append(line)

    return disc


def space_used(disc):
    used = 0
    for i in disc:
        used += Counter(i)[1]
    return used


disc = create_disc(data, 128)
used = space_used(disc)
print(f'Disc space used: {used}')