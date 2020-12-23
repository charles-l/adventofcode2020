from collections import Counter
import re

with open('input_day21') as f:
    lines = [x.strip() for x in f.readlines()]

potential_allergens = {}
parsed_lines = []
for l in lines:
    ingrediants_str, allergens_str = re.fullmatch(r'((?:\w+ )+)\(contains ((?:\w+)(?:, \w+)*)\)', l).groups()
    ingrediants = ingrediants_str.strip().split(' ')
    allergens = allergens_str.split(', ')
    parsed_lines.append((ingrediants, allergens))
    for a in allergens:
        if a not in potential_allergens:
            potential_allergens[a] = set(ingrediants)
        else:
            potential_allergens[a] = potential_allergens[a].intersection(set(ingrediants))

inert_ingrediants = set(sum((x[0] for x in parsed_lines), [])) - set.union(*potential_allergens.values())

m = {}

for ingrediants, allergens in parsed_lines:
    for a in allergens:
        if a not in m:
            m[a] = set(ingrediants) - inert_ingrediants
        else:
            m[a] = m[a].intersection(set(ingrediants) - inert_ingrediants)

to_clear = [k for k, x in m.items() if len(x) == 1]
while to_clear:
    a = to_clear.pop(0)
    i, = m[a]
    for k in m:
        if k == a or i not in m[k]:
            continue
        m[k].remove(i)
        if len(m[k]) == 1:
            to_clear.append(k)

print(','.join(list(x[1])[0] for x in sorted(m.items(), key=lambda x: x[0])))
