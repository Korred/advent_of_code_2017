with open('input.txt') as f:
    data = [line.strip("\n").split() for line in f.readlines()]


def duet(table):
    curr = 0
    last_played = None
    register = {k: 0 for k in set([t[1] for t in table]) if not k.isdigit()}

    operations = {
        "snd": lambda x: print(f"\tBeep #{x}"),
        "set": lambda x, y: register[y] if y in register else int(y),
        "add": lambda x, y: register[x] + register[y] if y in register else register[x] + int(y),
        "mul": lambda x, y: register[x] * register[y] if y in register else register[x] * int(y),
        "mod": lambda x, y: register[x] % register[y] if y in register else register[x] % int(y),
        "rcv": lambda x: print(f"Recovering last played sound: Beep #{last_played}") if x != 0 else print("Recover instruction ignored!"),
        "jgz": lambda x, y: print(f"Jumping {y} instructions!") if x > 0 else print("Jump instruction ignored!"),
    }

    while(curr < len(table)):
        op = table[curr][0]

        if op == "snd":
            x = table[curr][1]
            x = register[x] if x in register else int(x)
            operations[op](x)
            last_played = x

        if op in ("set", "add", "mul", "mod"):
            x, y = table[curr][1:]
            register[x] = operations[op](x, y)

        if op == "jgz":
            x, y = table[curr][1:]
            x = register[x]
            y = register[y] if y in register else int(y)
            operations[op](x, y)
            if x > 0:
                curr += y
                continue

        if op == "rcv":
            x = table[curr][1]
            operations[op](x)
            if x != 0:
                return last_played

        curr += 1

    return last_played


duet(data)