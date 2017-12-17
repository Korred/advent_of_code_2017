data = [722, 354]

def gen(val, mult, crit):
    while True:
        val = (val*mult) % 2147483647
        if val % crit == 0:
            yield val

def judge(data, cnt):
    gen_a, gen_b  = gen(data[0], 16807, 4), gen(data[1], 48271, 8)
    matched = 0

    for c in range(cnt):
        a = next(gen_a)
        len_a = len(bin(a)[2:])
        bin_a = bin(a)[2:][-16:] if len_a >=16 else '0'*(16 - len_a) + bin(a)[2:]

        b = next(gen_b)
        len_b = len(bin(b)[2:])
        bin_b = bin(b)[2:][-16:] if len_b >=16 else '0'*(16 - len_b) + bin(b)[2:]

        if bin_a == bin_b:
            matched += 1

    return matched


solution = judge(data, 5000000)
print(solution)
