import string

with open('input.txt') as f:
    data = [list(line.strip("\n")) for line in f.readlines()]

curr = [0, data[0].index("|")]
direction = "down"
letters = string.ascii_uppercase
found = []
steps = 0



def move_up_down(pos, d):
    if d == "down":
        pos[0] += 1

    elif d == "up":
        pos[0] -= 1


def move_left_right(pos, d):
    if d == "left":
        pos[1] -= 1
    if d == "right":
        pos[1] += 1


while(True):
    steps += 1
    if data[curr[0]][curr[1]] == "|":
        if direction in ["left","right"]:
            move_left_right(curr, direction)
        move_up_down(curr, direction)

    elif data[curr[0]][curr[1]] == "-":
        if direction in ["up","down"]:
            move_up_down(curr, direction)
        else:
            move_left_right(curr, direction)

    elif data[curr[0]][curr[1]] == "+":
        if direction in ["down", "up"]:
            if data[curr[0]][curr[1]+1] != " ":
                direction = "right"
                move_left_right(curr, direction)

            elif data[curr[0]][curr[1]-1] != " ":
                direction = "left"
                move_left_right(curr, direction)

        elif direction in ["left", "right"]:
            if data[curr[0]-1][curr[1]] != " ":
                direction = "up"
                move_up_down(curr, direction)

            elif data[curr[0]+1][curr[1]] != " ":
                direction = "down"
                move_up_down(curr, direction)
    
    elif data[curr[0]][curr[1]] in letters:
        found.append(data[curr[0]][curr[1]])
        if direction in ["down", "up"]:
            move_up_down(curr, direction)
        elif direction in ["left", "right"]:
            move_left_right(curr, direction)

    elif data[curr[0]][curr[1]] == " ":
        print(steps-1)
        break


