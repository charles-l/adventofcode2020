import hexy as hx
import numpy as np

with open('input_day24') as f:
    lines = [x.strip() for x in f.readlines()]

h = hx.HexMap()

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

def flip_by_rules(h):
    new_h = hx.HexMap()
    white_tiles_to_check = set()
    # black tiles
    for tile in h:
        ax_coords = np.array([tuple(map(int, tile.split(',')))])
        if h[ax_coords] == ['b']:
            ns = hx.cube_to_axial(hx.get_neighbor(hx.axial_to_cube(ax_coords), hx.ALL_DIRECTIONS))
            if h[ns].count('b') == 0 or h[ns].count('b') > 2:
                new_h[ax_coords] = 'w'
            else:
                new_h[ax_coords] = 'b'

            for n in ns:
                if h[n] == ['w'] or h[n] == []:
                    white_tiles_to_check.add(tuple(n))

    # white tiles
    for tile in white_tiles_to_check:
        ax_coords = np.array([tile])
        ns = hx.cube_to_axial(hx.get_neighbor(hx.axial_to_cube(ax_coords), hx.ALL_DIRECTIONS))
        if h[ns].count('b') == 2:
            new_h[ax_coords] = 'b'
    return new_h

for i in range(100):
    h = flip_by_rules(h)
print(list(h.values()).count('b'))
