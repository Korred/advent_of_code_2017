data = "199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192"

def knot_hash(data):
    lengths = list(bytearray(data, "ascii")) + [17, 31, 73, 47, 23]
    lst = list(range(256))
    curr = 0
    skip = 0

    for i in range(64):
        for l in lengths:

            if (curr+l) < 256:
                lst[curr:curr+l] = lst[curr:curr+l][::-1]
            else:
                front = 256 - curr
                end = l-front
                rev = (lst[curr:curr+front]+lst[0:end])[::-1]

                lst[curr:curr+front] = rev[0:front]
                lst[0:end] = rev[front:]

            curr = (curr + l + skip) % 256
            skip += 1

    # create dense hash
    dense = []
    for i in range(16):
        rng = lst[16*i:16*(i+1)]

        for r in range(15):
            rng[r+1] = rng[r] ^ rng[r+1]

        dense.append(rng[-1])

    #to hex
    res = "".join([hex(i)[2:] if len(hex(i)[2:]) == 2 else '0' + hex(i)[2:] for i in dense])

    return res


def main():
    kh = knot_hash(data)
    print("Solution:\t", kh)


if __name__ == "__main__":
    main()