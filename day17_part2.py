import itertools
puzzle_input = '''\
.#######
#######.
###.###.
#....###
.#..##..
#.#.###.
###..###
.#.#.##.\
'''

# NOTE: not using the defaultdict impl in collections
# because it will add the value to the dict on access
# which I *don't* want in this case because it'll grow the
# edges of the tensor on access
class defaultdict(dict):
    def __init__(self, default_val):
        self._default_val = default_val
        super().__init__(self)

    def __getitem__(self, k):
        if k in self:
            return super().__getitem__(k)
        else:
            return self._default_val

    # HACK
    def copy(self):
        obj = type(self).__new__(self.__class__)
        obj.__dict__.update(self.__dict__)
        return obj

dirs = list(x for x in itertools.product(*([(-1, 0, 1)] * 4)) if x != (0, 0, 0, 0))

def count_surrounding(world, p):
    x, y, z, w = p
    return sum(world[(x+dx, y+dy, z+dz, w+dw)] for dx, dy, dz, dw in dirs)


def run_iter(world):
    world_step = world.copy()
    minx = min(x for x, _, _, _ in world.keys())
    maxx = max(x for x, _, _, _ in world.keys())
    miny = min(y for _, y, _, _ in world.keys())
    maxy = max(y for _, y, _, _ in world.keys())
    minz = min(z for _, _, z, _ in world.keys())
    maxz = max(z for _, _, z, _ in world.keys())
    minw = min(w for _, _, _, w in world.keys())
    maxw = max(w for _, _, _, w in world.keys())

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                for w in range(minw - 1, maxw + 2):
                    p = x, y, z, w
                    if world[p] and count_surrounding(world, p) in (2, 3):
                        world_step[p] = 1
                    elif not world[p] and count_surrounding(world, p) == 3:
                        world_step[p] = 1

    return world_step

###

world = defaultdict(0)
starting_state = [[1 if c == '#' else 0 for c in x]
                  for x in puzzle_input.split('\n')]

for y in range(len(starting_state)):
    for x in range(len(starting_state[0])):
        world[(x, y, 0, 0)] = starting_state[y][x]

for i in range(6):
    world = run_iter(world)

print(sum(world.values()))
