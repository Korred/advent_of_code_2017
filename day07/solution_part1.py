import re

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


towers = createtowers(createprograms(data))

print(towers)


