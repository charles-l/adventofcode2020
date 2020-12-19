import re
from icecream import ic

with open('input_day18', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def parse(line):
    ts = [x for x in re.split(r'([ ()+*])', line) if x != ' ' and x != '']
    ts = [int(x) if x.isdigit() else x for x in ts]
    def parenthesize(toks):
        r = []
        while toks:
            if toks[0] == '(':
                sol, rest = parenthesize(toks[1:])
                r.append(sol)
                toks = rest
            elif toks[0] == ')':
                return r, toks[1:]
            else:
                r.append(toks[0])
                toks = toks[1:]
        return r, []
    return parenthesize(ts)[0]

def evaluate(expr):
    if isinstance(expr, list):
        if len(expr) >= 3:
            n1, op, n2, *rest = expr
            if op == '+':
                return evaluate([evaluate(n1) + evaluate(n2), *rest])
            if op == '*':
                return evaluate([evaluate(n1) * evaluate(n2), *rest])
            assert False, expr
        else:
            return evaluate(expr[0])
    elif isinstance(expr, int):
        return expr

print(sum(evaluate(parse(line)) for line in lines))
