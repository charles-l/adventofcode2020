import re

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
    assert len(mask) == 36
    for x in c[1:]:
        r = re.match('mem\[(\d+)\] = (\d+)', x)
        n = int(r.group(2))
        nn = int(''.join([b if m == 'X' else m for m, b in zip(mask, pad36(bin(n)))]), base=2)
        '''
        print(pad36(bin(n)))
        print(mask)
        print(pad36(bin(nn)))
        '''
        mem[int(r.group(1))] = nn

print(sum(mem.values()))
