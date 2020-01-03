with open('input.txt') as f:
    data = [tuple(map(int, line.strip().split(": "))) for line in f.readlines()]


def severity(obs):
    rng = obs[-1][0] + 1
    firewall = []
    curr = -1

    sev = 0

    # prepare firewall
    for i in range(rng):
        if obs[0][0] == i:
            firewall.append([1, obs[0][1], "down"])
            obs.pop(0)
        else:
            firewall.append([0, 0, 0])

    for layer in firewall:
        curr += 1

        if layer[0] == 1:
            sev += curr * layer[1]
    
        for layer in firewall:

            if layer[2] == "down":
                if layer[0] < layer[1]:
                    layer[0] += 1
                else:
                    layer[0] -= 1
                    layer[2] = "up"

            elif layer[2] == "up":
                if layer[0] > 1:
                    layer[0] -= 1
                else:
                    layer[0] += 1
                    layer[2] = "down"

    return (firewall, sev)


solution = severity(data)
print(f"Severity: {solution[1]}")
