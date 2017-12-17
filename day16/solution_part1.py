import string

with open('input.txt') as f:
    data = f.read().strip("\n").split(",")

programs = list(string.ascii_lowercase[0:16])

def dance(programs, moves):
    for m in moves:
        # Spin
        if m[0] == "s":
            i = int(m[1:])
            programs = programs[-i:] + programs[:-i]

        # Exchange
        if m[0] == "x":
            a, b = list(map(int, m[1:].split("/")))
            programs[a], programs[b] = programs[b], programs[a]

        # Partner
        if m[0] == "p":
            a, b = m[1:].split("/")
            ia = programs.index(a)
            ib = programs.index(b)
            programs[ia], programs[ib] = programs[ib], programs[ia]


    return programs


solution = dance(programs, data)
print("".join(solution))