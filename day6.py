from collections import Counter
with open('input_day6', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def split_list(lst, sep):
    cur_block = []
    for l in lst:
        if l == sep:
            yield cur_block
            cur_block = []
        else:
            cur_block.append(l)
    yield cur_block

total = 0
for group in split_list(lines, ''):
    c = Counter()
    for answers in group:
        c.update(answers)
    total += len(c)
print(total)

