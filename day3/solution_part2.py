def sum_adjacent(x, y, memory):
    tot = 0
    to_check = [y]

    # check if top is available
    if y != 0:
        to_check.append(y-1)
    
    # check if bottom is available
    if y < len(memory)-1:
        to_check.append(y+1)

    for i in to_check:
        # check left
        if x != 0:
            tot += memory[i][x-1]

        # check right
        if x < len(memory[i])-1:
            tot += memory[i][x+1]
        
        # check center
        if (i, x) != (y, x) and x < len(memory[i]):
            tot += memory[i][x]

    return tot


def spiral_first_bigger(size):
    # initial memory map
    memory = [[1]]
    cnt = 0

    # inital direction
    direction = "r"
    x = 0
    y = 0

    while cnt <= size:
        
        if direction == "r":
            x += 1
            cnt = sum_adjacent(x, y, memory)
            memory[y].append(cnt)

            if y == 0 or len(memory[y-1]) == x:
                direction = "u"

        elif direction == "u":
            if y == 0:
                memory = [[0]*len(memory[0])] + memory
                cnt = sum_adjacent(x, y, memory)
                memory[y][x] = cnt
                direction = "l"
            else:
                y -= 1
                cnt = sum_adjacent(x, y, memory)
                memory[y].append(cnt)

        elif direction == "l":
            if x == 0:
                for i, line in enumerate(memory):
                    memory[i] = [0] + line
                cnt = sum_adjacent(x, y, memory)
                memory[y][x] = cnt
                direction = "d"
            else:
                
                x -= 1
                cnt = sum_adjacent(x, y, memory)
                memory[y][x] = cnt

        elif direction == "d":
            
            if y == len(memory)-1:
                memory.append([0])
                direction = "r"

            y += 1
            cnt = sum_adjacent(x, y, memory)
            memory[y][x] = cnt

    return (memory, cnt)


memory = spiral_first_bigger(265149)

# solution
print(memory[1])
