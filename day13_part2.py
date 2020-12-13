'''
I legit have no clue exactly what I'm computing here. I
just noticed cyclic patterns in the output for each position
and wrote the following code to find an increment (inc) that
computed a solution more rapidly.
'''
with open('input_day13') as f:
    f = [x.strip() for x in f.readlines()]
available_lines = [(o, int(l)) for o, l in enumerate(f[1].split(',')) if l != 'x']

def draw_table(t, available_lines):
    print(' ' * len(str(t) + ': ') + ' '.join(f'{x[1]:04}' for x in available_lines))
    for i in range(t, t + max(x[0] for x in available_lines) + 1):
        print(f'{i}: ', end='')
        for o, l in available_lines:
            if i % l == 0:
                print('x    ', end='')
            else:
                print('.    ', end='')
        print('')

inc = available_lines[0][1]
t = inc
i = 1
while True:
    print(i, t, [(t % l) for _, l in available_lines])
    o, l = available_lines[i]
    if (t + o) % l == 0:
        # found a starting point for a cycle
        # now search for a new inc that eliminates the
        # cycle
        t1 = t + inc
        while (t1 + o) % l != 0:
            t1 += inc
        if t1 > t:
            inc = t1 - t
        i += 1

    if all((t + o) % l == 0 for o, l in available_lines):
        draw_table(t, available_lines)
        print('answer:', t)
        break
    t += inc
