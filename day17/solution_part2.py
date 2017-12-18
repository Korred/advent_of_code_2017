data = 371


def spinlock2(steps, end):
    pos, out = 0, 0
    for i in range(1, end + 1):
        pos = ((pos + steps) % i) + 1
        out = i if pos == 1 else out
    return out


solution = spinlock2(data, 50000000)
print(solution)