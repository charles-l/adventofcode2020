# for part two, I realized
# realized the general problem was actually better with linked lists and
# a fast hash table lookup and rewrote it entirely.
import time
import array
from llist import dllist, dllistnode

input_str = '942387615'
def circular_next(dllist, node):
    if not node.next:
        return dllist.first
    else:
        return node.next

def remove_node(lst, node):
    lst.remove(node)
    return node

cups = dllist([int(x) for x in input_str] + list(range(10, 1000000+1)))
moves = 10000000

lookup = {}
x = cups.first
while x:
    lookup[x.value] = x
    x = x.next

min_cup = min(lookup.keys())
max_cup = max(lookup.keys())

current_cup = cups.first
for m in range(moves):
    picked_up = [remove_node(cups, circular_next(cups, current_cup)) for _ in range(3)]

    destination_cup = current_cup.value - 1
    while destination_cup in (x.value for x in picked_up) or destination_cup < min_cup:
        destination_cup -= 1
        if destination_cup < min_cup:
            destination_cup = max_cup

    destination_cup_node = lookup[destination_cup]
    for x in reversed(picked_up):
        cups.insertnode(x, circular_next(cups, destination_cup_node))

    current_cup = circular_next(cups, current_cup)

print(circular_next(cups, lookup[1]).value * circular_next(cups, circular_next(cups, lookup[1])).value)
