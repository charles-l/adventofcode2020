with open('input_day12') as f:
    instructions = [x.strip() for x in f.readlines()]

pos = [0, 0]
rot = 90

for x in instructions:
    n = int(x[1:])
    if x[0] == 'N' or (x[0] == 'F' and rot == 0):
        pos[1] += n
    elif x[0] == 'S' or (x[0] == 'F' and rot == 180):
        pos[1] -= n
    elif x[0] == 'E' or (x[0] == 'F' and rot == 90):
        pos[0] += n
    elif x[0] == 'W' or (x[0] == 'F' and rot == 270):
        pos[0] -= n
    elif x[0] == 'R':
        rot = (rot + n) % 360
    elif x[0] == 'L':
        rot = (rot - n) % 360
    else:
        assert False, f"unhandled {x=}"


print(abs(pos[0]) + abs(pos[1]))
