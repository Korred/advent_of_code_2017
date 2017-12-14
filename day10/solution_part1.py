data = "199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192"
data = list(map(int, data.split(",")))


def knot_hash(lengths, lst_size):
    lst = list(range(lst_size))
    curr = 0
    skip = 0

    for l in lengths:

        if (curr+l) < lst_size:
            lst[curr:curr+l] = lst[curr:curr+l][::-1]
        else:
            front = lst_size-curr
            end = l-front
            rev = (lst[curr:curr+front]+lst[0:end])[::-1]

            lst[curr:curr+front] = rev[0:front]
            lst[0:end] = rev[front:]

        curr = (curr + l + skip) % lst_size
        skip += 1

    return lst


kh = knot_hash(data, 256)

print("Solution:", kh[0]*kh[1])