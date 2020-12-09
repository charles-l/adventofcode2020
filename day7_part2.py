import re
from collections import defaultdict

bags = re.compile('((?:\w+ )+)bags?')
with open('input_day7', 'r') as f:
    lines = [x.strip().split('contain') for x in f.readlines()]

contains = defaultdict(set)

for l in lines:
    outer_bag, inner_bags = re.match(bags, l[0]).group(1).strip(), re.findall(bags, l[1])
    inner_bags = [x.strip() for x in inner_bags]
    for b in inner_bags:
        contains[outer_bag].add(b)

counted = set()
def count_paths(k):
    if k == 'no other':
        return 0
    n, color = k.split(' ', 1)
    n = int(n)
    total = n + sum(n * (count_paths(x)) for x in contains[color])
    return total

print(count_paths('1 shiny gold') - 1)
