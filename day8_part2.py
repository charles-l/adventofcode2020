with open('input_day8') as f:
    lines = [x.strip() for x in f.readlines()]
    jmp_indices = [i for i, x in enumerate(lines) if x.startswith('jmp')]

def execute_instructions(instructions):
    pc = 0
    accumulator = 0

    visited = set()
    while True:
        if pc >= len(instructions):
            print('terminated without repeating')
            return True
        op, arg = instructions[pc].split(' ')
        print(f'{pc=} {accumulator=} {op=} {arg=}')
        if pc in visited:
            print('failed')
            return False
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

for i in jmp_indices:
    instructions = list(lines)
    instructions[i] = instructions[i].replace('jmp', 'nop')
    if execute_instructions(instructions):
        break
    print(i)
