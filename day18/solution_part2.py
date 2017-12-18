with open('input.txt') as f:
    data = [line.strip("\n").split() for line in f.readlines()]


def duet(table):
    curr = [0, 0]
    queue = [[], []]
    registers = [{k: 0 for k in set([t[1] for t in table]) if not k.isdigit()},
                 {k: 0 for k in set([t[1] for t in table]) if not k.isdigit()}]
    registers[0]['p'] = 0
    registers[1]['p'] = 1

    send_cnt = [0, 0]

    operations = {
        "snd": lambda x, r: print(f"(Program #{r}) Sending #{x}"),
        "set": lambda x, y, r: registers[r][y] if y in registers[r] else int(y),
        "add": lambda x, y, r: registers[r][x] + registers[r][y] if y in registers[r] else registers[r][x] + int(y),
        "mul": lambda x, y, r: registers[r][x] * registers[r][y] if y in registers[r] else registers[r][x] * int(y),
        "mod": lambda x, y, r: registers[r][x] % registers[r][y] if y in registers[r] else registers[r][x] % int(y),
        "rcv": lambda x, r: print(f"(Program #{r}) Recovering last send"),
        "jgz": lambda x, y, r: print(f"(Program #{r}) Jumping {y} instructions!") if x > 0 else print(f"(Program #{r}) Jump instruction ignored!"),
    }

    while(True):
        for r in range(2):
            while(curr[r] < len(table)):

                op = table[curr[r]][0]

                if op == "snd":
                    x = table[curr[r]][1]
                    x = registers[r][x] if x in registers[r] else int(x)
                    operations[op](x, r)
                    send_cnt[r] += 1
                    queue[(r+1) % 2].append(x)

                if op in ("set", "add", "mul", "mod"):
                    x, y = table[curr[r]][1:]
                    registers[r][x] = operations[op](x, y, r)

                if op == "jgz":
                    x, y = table[curr[r]][1:]
                    x = registers[r][x] if x in registers[r] else int(x)
                    y = registers[r][y] if y in registers[r] else int(y)
                    operations[op](x, y, r)
                    if x > 0:
                        curr[r] += y
                        continue

                if op == "rcv":
                    x = table[curr[r]][1]
                    
                    if queue[r]:
                        operations[op](x, r)
                        registers[r][x] = queue[r].pop(0)
                    else:
                        break

                curr[r] += 1



        if not queue[0] and not queue[1] and table[curr[0]][0] == "rcv" and table[curr[1]][0] == "rcv":
            print("DEADLOCK!")
            return send_cnt
    
        if curr[0] == len(table) and curr[1] == len(table):
            return send_cnt


solution = duet(data)
print(f"Sends from Program 0: {solution[0]} - Sends from Program 1: {solution[1]}")