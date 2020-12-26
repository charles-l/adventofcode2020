# cython: language_level=3
import array

# 0 is unused (hence the + 1)
upper_bound = (1000000 + 1)
next_arr = array.array('I', [0] * upper_bound)
input_list = list(map(int, '942387615'))

# tricky setup code... figure out how to simplify
for i in range(len(input_list)-1):
    next_arr[input_list[i]] = input_list[i+1]
next_arr[input_list[-1]] = 10
for i in range(10, 1000000):
    next_arr[i] = i+1
next_arr[-1] = 9
min_cup, max_cup = 1, 1000000

def remove_next(n):
    i = next_arr[n]
    next_arr[n] = next_arr[next_arr[n]]
    return i

def insert_next(node, n):
    next_arr[n] = next_arr[node]
    next_arr[node] = n

def do_computation():
    current_cup = 9
    moves = 10000000

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
