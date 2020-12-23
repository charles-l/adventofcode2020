from boltons.iterutils import split
with open('input_day22', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

p1_raw, p2_raw = split(lines, '')
p1 = tuple(map(int, p1_raw[1:]))
p2 = tuple(map(int, p2_raw[1:]))

def play_game(p1, p2):
    previous_iteration = set()
    while p1 and p2:
        if (p1, p2) in previous_iteration:
            return 'p1', (p1, p2)

        previous_iteration.add((p1, p2))

        (p1c, p1), (p2c, p2) = (p1[0], p1[1:]), (p2[0], p2[1:])
        if p1c <= len(p1) and p2c <= len(p2):
            winner, _ = play_game(p1[:p1c], p2[:p2c])
            if winner == 'p1':
                p1 = p1 + (p1c, p2c)
            else:
                assert winner == 'p2'
                p2 = p2 + (p2c, p1c)
        else:
            if p1c > p2c:
                p1 = p1 + (p1c, p2c)
            else:
                p2 = p2 + (p2c, p1c)

    if p1:
        return 'p1', (p1, p2)
    else:
        return 'p2', (p1, p2)

#print(play_game((43, 19), (2, 29, 14)))
_, (r1, r2) = play_game(p1, p2)
print(sum(a * b for a, b in zip(r1 + r2, reversed(range(1, len(r1 + r2)+1)))))
