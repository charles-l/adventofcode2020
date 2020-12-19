import re

with open('input_day18', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def tokenize(line):
    ts = [x for x in re.split(r'([ ()+*])', line) if x != ' ' and x != '']
    ts = [int(x) if x.isdigit() else x for x in ts]
    return ts

def expr_bp(toks, min_bp=0):
    lhs = toks.pop(0)
    if lhs == '(':
        lhs = expr_bp(toks, 0)
        tmp = toks.pop(0)
        assert tmp == ')'

    while toks:
        op = toks[0]
        tmp = infix_binding_power(op)
        if tmp is None:
            break

        l_bp, r_bp = tmp
        if l_bp < min_bp:
            break

        toks.pop(0)

        rhs = expr_bp(toks, r_bp)
        lhs = (op, lhs, rhs)

    return lhs

def infix_binding_power(op):
    if op == '+':
        return (3, 4)
    elif op == '*':
        return (1, 2)
    else:
        return None

def evaluate(expr):
    if isinstance(expr, int):
        return expr
    elif expr[0] == '+':
        return evaluate(expr[1]) + evaluate(expr[2])
    elif expr[0] == '*':
        return evaluate(expr[1]) * evaluate(expr[2])

print(sum(evaluate(expr_bp(tokenize(line))) for line in lines))
