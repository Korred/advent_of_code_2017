with open('input.txt') as f:
    data = [tuple(map(int, line.strip().split(": "))) for line in f.readlines()]


def move_firewall(firewall, steps):
    for s in range(steps):
        for layer in firewall:

                if layer[3] == 1:
                    if layer[1] < layer[2]:
                        layer[1] += 1
                    else:
                        layer[1] -= 1
                        layer[3] = -1

                elif layer[3] == -1:
                    if layer[1] > 1:
                        layer[1] -= 1
                    else:
                        layer[1] += 1
                        layer[3] = 1


def severity(obs):
    init_firewall = []


    # prepare firewall once
    for o in obs:
        init_firewall.append([o[0], 1, o[1], 1])

    print(init_firewall)
    delay = 0
    while(True):
        
        move_firewall(init_firewall, 3873661)
        firewall = list(init_firewall)
        cought = False
        for e, layer in enumerate(firewall):

            if not e == layer[0]:
                move_firewall(firewall, layer[0]-e)
            print(layer)
            if layer[1] == 1:
                print(layer)
                cought = True
                break
        
            move_firewall(firewall, 1)

        if cought:
            delay += 1
        else:
            return delay

    

solution = severity(data)
print(f"Smallest delay to not get cought: {solution}")
