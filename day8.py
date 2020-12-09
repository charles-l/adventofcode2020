with open('input_day8') as f:
    lines = [x.strip() for x in f.readlines()]
    jmp_indices = [i for i, x in enumerate(lines) if x.startswith('jmp')]

pc = 0
accumulator = 0

visited = set()
while True:
    op, arg = lines[pc].split(' ')
    print(f'{pc=} {accumulator=} {op=} {arg=}')
    if pc in visited:
        break
    visited.add(pc)
    arg = int(arg)
    if op == 'jmp':
        pc += arg
        continue
    elif op == 'nop':
        pass
    elif op == 'acc':
        accumulator += arg
    pc += 1

