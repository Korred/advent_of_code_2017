data = [722, 354]

def judge(data, cnt):
    a, b  = data
    matched = 0

    for c in range(cnt):
        if c % (cnt//100) == 0:
            print(c)
        a = (a*16807) % 2147483647
        b = (b*48271) % 2147483647

        len_a = len(bin(a)[2:])
        len_b = len(bin(b)[2:])
        bin_a = bin(a)[2:][-16:] if len_a >=16 else '0'*(16 - len_a) + bin(a)[2:]
        bin_b = bin(b)[2:][-16:] if len_b >=16 else '0'*(16 - len_b) + bin(b)[2:]

        if bin_a == bin_b:
            matched += 1

    return matched


solution = judge(data, 40000000)
print(solution)