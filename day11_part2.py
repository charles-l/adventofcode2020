import sys
with open('input_day11', 'r') as f:
    seatmap = [x.strip() for x in f.readlines()]

def n_occupied_around(m, pos):
    ds = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    n = 0
    for d in ds:
        i = 1
        while True:
            x = pos[0] + d[0] * i
            y = pos[1] + d[1] * i
            if not (0 <= y < len(m) and 0 <= x < len(m[0])):
                break
            if m[y][x] == '#':
                n += 1
                break
            if m[y][x] == 'L':
                break
            i += 1
    return n

def run_iter(m):
    r = list([list(x) for x in m])
    for j in range(len(m)):
        for i in range(len(m[0])):
            if m[j][i] == 'L':
                if n_occupied_around(m, (i, j)) == 0:
                    r[j][i] = '#'
                else:
                    r[j][i] = 'L'
            elif m[j][i] == '#':
                if n_occupied_around(m, (i, j)) >= 5:
                    r[j][i] = 'L'
                else:
                    r[j][i] = '#'
            elif m[j][i] == '.':
                r[j][i] = '.'

    print('')
    print('\n'.join([''.join(x) for x in r]))

    return r

m = seatmap
while True:
    m1 = run_iter(m)
    if m == m1:
        break
    m = m1

print(sum(sum(1 for x in r if x == '#') for r in m))
