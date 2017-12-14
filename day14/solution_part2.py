from collections import Counter
import string
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
        

def get_regions(disc):
    regions = 0
    seen = set()
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    s = 0
    region_symbols = string.ascii_uppercase + string.punctuation

    for y, row in enumerate(disc):
        for x, entry in enumerate(row):
            if (x, y) not in seen and disc[y][x] == 1:
                regions += 1
                to_check = [(x, y)]
                seen.add((x, y))
                disc[y][x] = region_symbols[s]
                

                # iterative bfs
                while(to_check):
                    
                    e = to_check.pop()
                    
                    for d in dirs:
                        n = (e[0] + d[0], e[1] + d[1])
                        if (n[0] >= 0) and (n[0] < len(row)) and (n[1] >= 0) and (n[1] < len(disc)):
                            #rint(f"Disc lengths: {len(disc)} {len(row)} - Requested pos: {n[1]} {n[0]}")
                            if disc[n[1]][n[0]] == 1 and n not in seen:
                                to_check.append(n)
                                seen.add(n)
                                disc[n[1]][n[0]] = region_symbols[s]

                s = s+1 if s+1 < len(region_symbols) else 0

    return (regions, disc)


disc = create_disc(data, 128)
regions = get_regions(disc)

print(f'Disc with regions:')
for line in disc:
    print("".join(map(str, line)))

print()
print(f'Regions found: {regions[0]}')

