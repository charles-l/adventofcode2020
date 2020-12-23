from collections import Counter
import re

with open('input_day21') as f:
    lines = [x.strip() for x in f.readlines()]

m = {}
ingrediant_counts = Counter()
for l in lines:
    ingrediants_str, allergens_str = re.fullmatch(r'((?:\w+ )+)\(contains ((?:\w+)(?:, \w+)*)\)', l).groups()
    ingrediants = ingrediants_str.strip().split(' ')
    ingrediant_counts.update(ingrediants)
    allergens = allergens_str.split(', ')
    for a in allergens:
        if a not in m:
            m[a] = set(ingrediants)
        else:
            m[a] = m[a].intersection(set(ingrediants))

for g in set.union(*list(m.values())):
    del ingrediant_counts[g]

print(sum(ingrediant_counts.values()))
