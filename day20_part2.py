# ugggg soooo much code for this solution and it's gross...
# this took *way* longer to solve than it should have
import re
import math
from collections import defaultdict
from boltons.iterutils import split
import operator as op
with open('input_day20') as f:
    tiles = {int(re.fullmatch(r'Tile (\d+):', chunk[0]).group(1)): chunk[1:]
             for chunk in (split((x.strip() for x in f.readlines()), '',))}

top_edge = lambda tile: ''.join(tile[0])
bottom_edge = lambda tile: ''.join(tile[-1])
left_edge = lambda tile: ''.join(r[0] for r in tile)
right_edge = lambda tile: ''.join(r[-1] for r in tile)
edges = lambda tile: {top_edge(tile), bottom_edge(tile), left_edge(tile), right_edge(tile)}
flipped_edges = lambda tile: {x[::-1] for x in edges(tile)}
any_edges = lambda tile: edges(tile).union(flipped_edges(tile))

tile_names = list(tiles.keys())
tile_index = {y: x for x, y in enumerate(tile_names)}

tile_edges = defaultdict(set)
for t, grid in tiles.items():
    ps = [top_edge(grid), right_edge(grid), bottom_edge(grid), left_edge(grid)]
    ps += [x[::-1] for x in ps]
    for p in ps:
        tile_edges[p].add(t)

M = [[0 for _ in range(len(tile_index))] for _ in range(len(tile_index))]

for edge_set in tile_edges.values():
    if len(edge_set) == 2:
        a, b = edge_set
        i, j = tile_index[a], tile_index[b]
        M[i][j] = M[j][i] = 1

length = int(math.sqrt(len(tiles)))
corners = [tile_names[i] for i, r in enumerate(M) if sum(r) == 2]

def connected(node):
    return {tile_names[i] for i, m in enumerate(M[tile_index[node]]) if m == 1}

def rotate(tile):
    assert len(tile) == len(tile[0])
    r = [[None for _ in r] for r in tile]
    for j in range(len(tile)):
        for i in range(len(tile[0])):
            r[i][len(tile[0])-j-1] = tile[j][i]
    return r

def flip(tile):
    return tile[::-1]

def str_tile(tile):
    return '\n'.join(''.join(x for x in r) for r in tile)

def merge_tiles(map_tiles):
    x = []
    for j in range(len(map_tiles)):
        for k in range(len(map_tiles[0][0])):
            x.append([])
            for i in range(len(map_tiles[0])):
                if map_tiles[j][i] is None:
                    x[-1].extend([' '] * len(map_tiles[0][0][0]))
                else:
                    x[-1].extend(map_tiles[j][i][k])
    return x

map_ids = [[None for _ in range(length)] for _ in range(length)]
map_tiles = [[None for _ in range(length)] for _ in range(length)]

# set first corner
map_ids[0][0] = corners[0]
map_ids[0][1], map_ids[1][0] = connected(corners[0])
used = {map_ids[0][0], map_ids[0][1], map_ids[1][0]}

def transform_until(tile, right=None, left=None, top=None):
    check_p = None

    if top is not None:
        if isinstance(top, set):
            check_p = lambda t: top_edge(t) in top
        elif isinstance(top, str):
            check_p = lambda t: top_edge(t) == top

    if left is not None:
        if isinstance(left, set):
            check_p = lambda t: left_edge(t) in left
        elif isinstance(left, str):
            check_p = lambda t: left_edge(t) == left

    if right is not None:
        if isinstance(right, set):
            check_p = lambda t: right_edge(t) in right
        elif isinstance(right, str):
            check_p = lambda t: right_edge(t) == right

    assert check_p, (check_p, right, left, top)

    # all possible transforms
    transforms = [rotate] * 4 + [flip] + [rotate] * 4
    while transforms:
        tile = transforms.pop(0)(tile)
        if check_p(tile):
            return tile

    assert False, f'failed on {top=} {right=} {left=}\n' + str_tile(tile)

if __name__ == '__main__':
    map_tiles[0][0] = transform_until(tiles[map_ids[0][0]], right=any_edges(tiles[map_ids[0][1]]))

    map_tiles[0][1] = transform_until(tiles[map_ids[0][1]], left=right_edge(map_tiles[0][0]))
    map_tiles[1][0] = tiles[map_ids[1][0]]

    if bottom_edge(map_tiles[0][0]) not in any_edges(map_tiles[1][0]):
        map_tiles[0][0], map_tiles[0][1] = flip(map_tiles[0][0]), flip(map_tiles[0][1])

    map_tiles[1][0] = transform_until(map_tiles[1][0], top=bottom_edge(map_tiles[0][0]))

    assert bottom_edge(map_tiles[0][0]) in edges(map_tiles[1][0]), "??"

    map_tiles[1][0] = transform_until(tiles[map_ids[1][0]], top=bottom_edge(map_tiles[0][0]))

    for j in range(len(map_tiles)):
        for i in range(len(map_tiles[0])):
            if map_tiles[j][i] is None:
                if i > 0:
                    candidates = connected(map_ids[j][i-1]) - used
                    if len(candidates) == 2:
                        candidate_a, candidate_b = candidates
                        if right_edge(map_tiles[j][i-1]) in edges(tiles[candidate_a]).union(flipped_edges(tiles[candidate_a])):
                            map_ids[j][i] = candidate_a
                        else:
                            assert right_edge(map_tiles[j][i-1]) in edges(tiles[candidate_b]).union(flipped_edges(tiles[candidate_b]))
                            map_ids[j][i] = candidate_b
                    else:
                        assert len(candidates) == 1
                        candidate, = candidates
                        map_ids[j][i] = candidate
                    map_tiles[j][i] = transform_until(tiles[map_ids[j][i]], left=right_edge(map_tiles[j][i-1]))
                else:
                    candidates = connected(map_ids[j-1][i]) - used
                    if len(candidates) == 2:
                        candidate_a, candidate_b = candidates
                        if bottom_edge(map_tiles[j][i-1]) in edges(tiles[candidate_a]).union(flipped_edges(tiles[candidate_a])):
                            map_ids[j][i] = candidate_a
                        else:
                            assert bottom_edge(map_tiles[j][i-1]) in edges(tiles[candidate_b]).union(flipped_edges(tiles[candidate_b]))
                            map_ids[j][i] = candidate_b
                    else:
                        assert len(candidates) == 1
                        candidate, = candidates
                        map_ids[j][i] = candidate
                    map_tiles[j][i] = transform_until(tiles[map_ids[j][i]], top=bottom_edge(map_tiles[j-1][i]))
                used.add(map_ids[j][i])

    for r in map_tiles:
        for i, t in enumerate(r):
            r[i] = [r[1:-1] for r in t[1:-1]]
    print(str_tile(merge_tiles(map_tiles)))

    mask_str = '''\
                  #
#    ##    ##    ###
 #  #  #  #  #  #\
'''.split('\n')
    full_len = max(len(m) for m in mask_str)
    mask = [list(x + ' ' * (full_len - len(x))) for x in mask_str]
    map_tiles = merge_tiles(map_tiles)
    for op in [rotate, rotate, rotate, rotate, flip, rotate, rotate, rotate, rotate]:
        map_tiles = op(map_tiles)
        nmonsters = 0
        for i in range(len(map_tiles) - len(mask) + 1):
            for j in range(len(map_tiles[0]) - len(mask[0]) + 1):
                for ii, mask_row in enumerate(mask):
                    if not all(x == y for x, y in zip(mask_row, map_tiles[i+ii][j:]) if x == '#'):
                        break
                else:
                    nmonsters += 1
        if nmonsters:
            break

    print(sum(x.count('#') for x in map_tiles) - (nmonsters * sum(m.count('#') for m in mask_str)))
