import re
from collections import defaultdict

bags = re.compile('((?:[a-zA-Z]+ )+)bags?')
with open('input_day7', 'r') as f:
    lines = [x.strip().split('contain') for x in f.readlines()]

contained_by = defaultdict(set)

for l in lines:
    outer_bag, inner_bags = re.match(bags, l[0]).group(1).strip(), re.findall(bags, l[1])
    inner_bags = [x.strip() for x in inner_bags]
    for b in inner_bags:
        contained_by[b].add(outer_bag)

counted = set()
def count_paths(k):
    if k in counted:
        return 0
    counted.add(k)
    return 1 + sum(count_paths(x) for x in contained_by[k])

print(count_paths('shiny gold') - 1)
