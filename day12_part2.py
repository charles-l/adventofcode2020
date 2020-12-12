with open('input_day12') as f:
    instructions = [x.strip() for x in f.readlines()]

pos = [0, 0]
waypoint_pos = [10, 1]

for x in instructions:
    n = int(x[1:])
    if x[0] == 'N':
        waypoint_pos[1] += n
    elif x[0] == 'S':
        waypoint_pos[1] -= n
    elif x[0] == 'E':
        waypoint_pos[0] += n
    elif x[0] == 'W':
        waypoint_pos[0] -= n
    elif x[0] == 'F':
        for i in range(n):
            pos[0] += waypoint_pos[0]
            pos[1] += waypoint_pos[1]
    elif x[0] == 'R':
        '''
        rotate 90 degrees:

        v * (0  1
             -1 0)
        '''
        assert n % 90 == 0
        for i in range(n // 90):
            waypoint_pos[0], waypoint_pos[1] = waypoint_pos[1], -waypoint_pos[0]
    elif x[0] == 'L':
        '''
        rotate -90 degrees:

        v * (0 -1
             1  0)
        '''
        assert n % 90 == 0
        for i in range(n // 90):
            waypoint_pos[0], waypoint_pos[1] = -waypoint_pos[1], waypoint_pos[0]
    else:
        assert False, f"unhandled {x=}"
    print(pos, waypoint_pos)


print(abs(pos[0]) + abs(pos[1]))
