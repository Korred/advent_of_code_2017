def spiral_memory_maker(size):
    memory = [[1]]
    cnt = 2
    direction = "r"
    x = 0
    y = 0

    while cnt <= size:
        if direction == "r":
            memory[y].append(cnt)
            x += 1

            if y == 0 or len(memory[y-1]) == x:
                direction = "u"

        elif direction == "u":
            if y == 0:
                memory = [[0]*len(memory[0])] + memory
                memory[y][x] = cnt
                direction = "l"
            else:
                memory[y-1].append(cnt)
                y -= 1    


        elif direction == "l":
            if x == 0:
                for i, line in enumerate(memory):
                    memory[i] = [0] + line
                    
                memory[y][x] = cnt
                direction = "d"
            else:
                memory[y][x-1] = cnt
                x -= 1 

        elif direction == "d":
            
            if y == len(memory)-1:
                memory.append([cnt])
                direction = "r"

            memory[y+1][x] = cnt
            y += 1

        
        cnt += 1
    return memory

def find(address, memory):
    for i, line in enumerate(memory):
        for j, entry in enumerate(line):
            if entry == address:
                return (i, j)
    return (None, None)

def taxicab(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

memory = spiral_memory_maker(265149)
start = find(265149, memory)
end = find(1, memory)

# solution
print(taxicab(start, end))