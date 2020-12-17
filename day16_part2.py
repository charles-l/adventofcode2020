import re
from functools import reduce
import operator as op

with open('input_day16', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

idxs = [i for i, x in enumerate(lines) if x == '']
rules_str = lines[:idxs[0]]
ticket = [int(x) for x in lines[idxs[0]+2:idxs[1]][0].split(',')]
nearby_tickets_str = lines[idxs[1]+2:]

rules = {}
for r in rules_str:
    m = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', r)
    rules[m.group(1)] = [(int(m.group(2)), int(m.group(3))),
                           (int(m.group(4)), int(m.group(5)))]

tickets = [list(map(int, x.split(','))) for x in nearby_tickets_str]

valid_tickets = []
for t in tickets:
    for v in t:
        valid_ticket = any(p1 <= v <= p2 for p1, p2 in sum(rules.values(), []))
        if not valid_ticket:
            break
    else:
        valid_tickets.append(t)

candidate_positions = []
for rule_name, ranges in rules.items():
    assert len(ranges) == 2, ranges
    (l1, u1), (l2, u2) = ranges
    cur_candidate_positions = []
    for i in range(len(valid_tickets[0])):
        if all(l1 <= t[i] <= u1 or l2 <= t[i] <= u2 for t in valid_tickets):
            cur_candidate_positions.append(1)
        else:
            cur_candidate_positions.append(0)
    candidate_positions.append(cur_candidate_positions)

for r, ps in zip(rules.keys(), candidate_positions):
    print(' '.join(map(str, ps)), r)
print('')

from constraint import Problem, AllDifferentConstraint
problem = Problem()
for r, ps in zip(rules.keys(), candidate_positions):
    problem.addVariable(r, [i for i, x in enumerate(ps) if x == 1])
problem.addConstraint(AllDifferentConstraint())
solved_positions = problem.getSolutions()
assert len(solved_positions) == 1

for r in rules.keys():
    mask = [0] * len(rules)
    mask[solved_positions[0][r]] = 1
    print(' '.join(map(str, mask)), r)

departure_keys = [k for k in rules.keys() if k.startswith('departure')]

print('solution', reduce(op.mul, (ticket[solved_positions[0][k]] for k in departure_keys)))
