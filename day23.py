# crappy first attempt (with lots of edge cases fixed by hand, which makes it prone to bugs)
cups = [int(x) for x in '942387615']
min_cup = min(cups)
max_cup = max(cups)
moves = 100

# wraps i
def get(i):
    return cups[i % len(cups)]

def get_range(i, j):
    assert j >= i
    return [cups[k % len(cups)] for k in range(i, j)]

current_cup = cups[0]
for m in range(moves):
    i = cups.index(current_cup)
    picked_up = get_range(i+1, i+4)
    destination_cup = current_cup - 1
    while destination_cup in picked_up or destination_cup < min_cup:
        destination_cup -= 1
        if destination_cup < min_cup:
            destination_cup = max_cup

    for j in range(i+1, i+4):
        cups[j%len(cups)] = None
    cups = [c for c in cups if c is not None]

    destination_cup_i = cups.index(destination_cup)
    for x in reversed(picked_up):
        cups.insert(destination_cup_i+1, x)
    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]


start = cups.index(1)
print(''.join(str(cups[(start + i) % len(cups)]) for i in range(1, len(cups))))
