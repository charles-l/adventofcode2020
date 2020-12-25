import hexy as hx
import numpy as np

with open('input_day24') as f:
    lines = [x.strip() for x in f.readlines()]

h = hx.HexMap()
#h[[(0, 0)]] = ['w']

for l in lines:
    i = 0
    dirs = []
    while i < len(l):
        if l[i] in ('s', 'n'):
            dirs.append(l[i:i+2])
            i += 2
        else:
            dirs.append(l[i])
            i += 1

    cur_pos = np.array([(0, 0, 0)])
    for d in dirs:
        dx = getattr(hx, d.upper())
        cur_pos = hx.get_neighbor(cur_pos, dx)
    a = hx.cube_to_axial(cur_pos)
    if h[a] == ['b']:
        h.overwrite_entries(a, 'w')
    else:
        h[a] = 'b'

print(list(h.values()).count('b'))
