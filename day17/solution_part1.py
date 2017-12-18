data = 371


def spinlock(steps, end):
    sl = [0]
    pos = 0

    for i in range(1, end + 1):
        pos = ((pos + steps) % i) + 1
        sl = sl[:pos] + [i] + sl[pos:]

    return sl


sl = spinlock(data, 2017)
solution = sl[sl.index(2017) + 1]
print(solution)
