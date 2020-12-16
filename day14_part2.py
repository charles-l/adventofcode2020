import re
import itertools

with open('input_day14', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def chunks(lst):
    i = 0
    chunk = []
    while i < len(lst)-1:
        chunk.append(lst[i])
        if lst[i+1].startswith('mask'):
            yield chunk
            chunk = []

        i += 1
    chunk.append(lst[-1])
    yield chunk

def pad36(bstr):
    prefixlen = 36 - (len(bstr) - 2)
    return ('0' * prefixlen) + bstr[2:]

mem = {}

for c in chunks(lines):
    mask = c[0].split()[2]
    ix = [i for i, b in enumerate(mask) if b == 'X']

    assert len(mask) == 36
    for x in c[1:]:
        match = re.match('mem\[(\d+)\] = (\d+)', x)
        addr = int(match.group(1))
        val = int(match.group(2))

        pass1 = ''.join(['1' if m == '1' else b for m, b in zip(mask, pad36(bin(addr)))])

        for bb in itertools.product(*(((0,1),) * len(ix))):
            addr_mod = [*pass1]
            for i, b in zip(ix, bb):
                addr_mod[i] = str(b)
            mem[int(''.join(addr_mod), 2)] = val

print(sum(mem.values()))
