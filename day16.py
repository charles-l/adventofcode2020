import re

with open('input_day16', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

idxs = [i for i, x in enumerate(lines) if x == '']
rules_str = lines[:idxs[0]]
ticket = lines[idxs[0]+2:idxs[1]]
nearby_tickets_str = lines[idxs[1]+2:]

rules = {}
for r in rules_str:
    m = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', r)
    rules[m.group(1)] = [(int(m.group(2)), int(m.group(3))),
                           (int(m.group(4)), int(m.group(5)))]

tickets = [list(map(int, x.split(','))) for x in nearby_tickets_str]

err = 0
for t in tickets:
    for v in t:
        if not any(p1 <= v <= p2 for p1, p2 in sum(rules.values(), [])):
            err += v

print(err)
