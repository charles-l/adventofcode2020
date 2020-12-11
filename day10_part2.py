from functools import reduce
import operator as op

'''
brute forced it by hand lol

 3 3
1 4 7

 3 1 3
1 4 5 8

 3 1 1 3
1 4 5 6 9
1 4   6 9

 3 1 1 1 3
1 4 5 6 7 10
1 4   6 7 10
1 4 5   7 10
1 4     7 10

 3 1 1 1 1 3
1 4 5 6 7 8 11
1 4   6 7 8 11
1 4 5   7 8 11
1 4     7 8 11
1 4 5 6   8 11
1 4   6   8 11
1 4 5     8 11

Note that this case doesn't work, because 8-4 = 4, not 3:
1 4       8 11

And apparently in my puzzle input I never had more than 4
runs of 1, so I just used a lookup table to solve it :P
'''

m = {
    0: 1,
    1: 1,
    2: 2,
    3: 4,
    4: 7,
    }

with open('input_day10', 'r') as f:
    nums = sorted([int(x.strip()) for x in f.readlines()])

def split_list(l, target):
    r = []
    for x in l:
        if x == target:
            yield r
            r = []
        else:
            r.append(x)
    yield r

nums = [0] + nums + [nums[-1] + 3]
ds = [x - y for x,y in zip(nums[1:], nums[:-1])]
assert(set(ds) == {1, 3})  # we only handle deltas of 1 and 3
print(reduce(op.mul, (m[len(x)] for x in split_list(ds, 3))))
