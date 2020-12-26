# cython: language_level=3
from cpython cimport array
import itertools
import array

# 0 is unused (hence the + 1)
upper_bound = (1000000 + 1)
cdef array.array next_arr = array.array('I', [0] * upper_bound)
input_list = list(map(int, '942387615'))

for a, b in zip(itertools.chain(input_list, range(10, upper_bound)),
                itertools.chain(input_list[1:], range(10, upper_bound))):
    next_arr[a] = b
next_arr[-1] = 9

min_cup, max_cup = 1, 1000000

cdef int remove_next(int n):
    i = next_arr[n]
    next_arr[n] = next_arr[next_arr[n]]
    return i

cdef int insert_next(int node, int n):
    next_arr[n] = next_arr[node]
    next_arr[node] = n

def do_computation():
    cdef int current_cup = 9
    cdef int moves = 10000000

    for m in range(moves):
        picked_up = [remove_next(current_cup) for _ in range(3)]
        dest_cup = current_cup - 1
        while dest_cup in picked_up or dest_cup < min_cup:
            dest_cup -= 1
            if dest_cup < min_cup:
                dest_cup = max_cup

        for x in reversed(picked_up):
            insert_next(dest_cup, x)
        current_cup = next_arr[current_cup]

    return next_arr[1] * next_arr[next_arr[1]]
