# stayed up 'til 12:00 to write this code so it's a bit gross
# it wasn't worth it (-_-)

with open('input_day5', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def parse(line):
    l, u = 0, 127
    for i in range(7):
        if line[i] == 'F':
            u -= (u - l) // 2 + 1
        if line[i] == 'B':
            l += (u - l) // 2 + 1
    row = l

    l, u = 0, 7
    for i in range(3):
        if line[7+i] == 'L':
            u -= (u - l) // 2 + 1
        if line[7+i] == 'R':
            l += (u - l) // 2 + 1
    col = l

    return row, col

xs = [parse(l) for l in lines]
print(max(x[0] * 8 + x[1] for x in xs))
