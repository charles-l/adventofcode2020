import re
from collections import defaultdict
from boltons.iterutils import split
from functools import reduce, partial
import operator as op
with open('input_day20') as f:
    tiles = {int(re.fullmatch(r'Tile (\d+):', chunk[0]).group(1)): chunk[1:]
             for chunk in (split((x.strip() for x in f.readlines()), '',))}

tile_names = list(tiles.keys())
tile_index = {y: x for x, y in enumerate(tile_names)}

tile_edges = defaultdict(set)
for t, grid in tiles.items():
    ps = [grid[0], ''.join([r[-1] for r in grid]), grid[-1], ''.join([r[0] for r in grid])]
    ps += [x[::-1] for x in ps]
    for p in ps:
        tile_edges[p].add(t)

M = [[0 for _ in range(len(tile_index))] for _ in range(len(tile_index))]

for edge_set in tile_edges.values():
    if len(edge_set) == 2:
        a, b = edge_set
        i, j = tile_index[a], tile_index[b]
        M[i][j] = M[j][i] = 1

#print(tile_index)
#print('\n'.join(' '.join(map(str, x)) for x in M))
product = partial(reduce, op.mul)
print(product([tile_names[i] for i, r in enumerate(M) if sum(r) == 2]))
