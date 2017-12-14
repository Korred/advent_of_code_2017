data = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3".split("\t")
data = list(map(int, data))


def mem_realloc(memory):
    seen = set()
    cnt = 0
    mem_len = len(memory)

    # check/save currenty memory config, find max, set to 0 and redistribute blocks
    while(tuple(memory) not in seen):
        # add currenty memory config
        seen.add(tuple(memory))

        i = memory.index(max(memory))
        j = i + 1
        m = max(memory)

        # first set memory bank blocks to 0
        memory[i] = 0

        # redistribute blocks
        while(m != 0):
            memory[j % mem_len] += 1
            j += 1
            m -= 1

        cnt += 1

    return (memory, cnt)


res1 = mem_realloc(data)
print(mem_realloc(res1[0]))
