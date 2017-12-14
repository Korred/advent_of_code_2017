import re
from collections import Counter

with open("input.txt") as f:
    data = f.readlines()


class program(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def __str__(self):
        try:
            children = "\t".join(self.children)
        except TypeError:
            children = "\t".join([c.name for c in self.children])
        return "{}\t\t({})\t->\t{}".format(self.name, self.weight, children)

    def __repr__(self): 
        return "Program - {} ({})".format(self.name, self.weight)


def createprograms(data):
    programs = []
    for line in data:
        entry = re.sub('[()>,-]', '', line).strip().split()
        prg = program(entry[0], int(entry[1]), [i for i in entry[2:]]) 
        programs.append(prg)

    programs.sort(key=lambda x: len(x.children))
    return programs


def createtowers(programs):
    towers = {}

    while(programs):
        to_del = []
        for p in programs:
            if not p.children:
                towers[p.name] = p
                to_del.append(p.name)
                continue

            if all(prog in towers for prog in p.children):
                p.children = [towers[c] for c in p.children]

                towers[p.name] = p
                for c in p.children:
                    del towers[c.name]
                to_del.append(p.name)

        programs = [p for p in programs if p.name not in to_del]

    return towers


def check_weights(prog):
    progs = []

    for child in prog.children:
        p = check_weights(child)
        progs.append(p)

    progs.sort(key=lambda x: x[0])

    cnt = Counter([p[0] for p in progs])
    if len(cnt) > 1:

        least = cnt.most_common()[-1][0]
        most = cnt.most_common()[0][0]
        print(least, most)
        diff = abs(least-most)

        bad_prog = None
        for p in progs:
            if p[0] == least:
                bad_prog = p[1]

        if least > most:
            fix_weight = bad_prog.weight - diff
        else:
            fix_weight = bad_prog.weight + diff
        
        err = "Program {} is not correctly weighted! Adjust weight from {} to {}".format(bad_prog.name, bad_prog.weight, fix_weight)
        raise Exception(err)

    else:
        return (prog.weight + sum(p[0] for p in progs), prog)


towers = createtowers(createprograms(data))

check_weights(towers["cyrupz"])


