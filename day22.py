from boltons.iterutils import split
with open('input_day22', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

p1_raw, p2_raw = split(lines, '')
p1 = list(map(int, p1_raw[1:]))
p2 = list(map(int, p2_raw[1:]))

while p1 and p2:
    p1c, p2c = p1.pop(0), p2.pop(0)
    if p1c > p2c:
        p1.extend([p1c, p2c])
    else:
        p2.extend([p2c, p1c])

print(sum(a * b for a, b in zip(p1 + p2, reversed(range(1, len(p1 + p2)+1)))))
