import re

with open("input.txt") as f:
    data = [d.split() for d in f.readlines()]


def run_instructions(inst):
    operations = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        "<": lambda x, y: x < y,
        ">": lambda x, y: x > y,
        "<=": lambda x, y: x <= y,
        ">=": lambda x, y: x >= y,
    }

    register = {}
    for i in inst:
        a = i[0]
        b = i[4]
        op = i[1]
        comp = i[5]
        val = int(i[2])

        if a not in register:
            register[a] = 0

        if b not in register:
            register[b] = 0

        if operations[comp](register[b], int(i[6])):
            register[a] = register[a] + val if op == "inc" else register[a] - val

    return register


register = run_instructions(data)

solution = register[max(register, key=register.get)]
print(solution)

