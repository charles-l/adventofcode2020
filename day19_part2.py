from boltons.iterutils import split
import re
with open('test_day19') as f:
    lines = [x.strip() for x in f.readlines()]

raw_rules = lines[:lines.index('')]
messages = lines[lines.index('')+1:]

def convert_to_type(s):
    if s.isdigit():
        return int(s)
    elif s[0] == '"':
        return s.replace('"', '')
    else:
        assert False, repr(s)

# parse
rules = {}
for r in raw_rules:
    toks = [x for x in re.split(r'(".*?"|\W)', r) if x != '' and x != ' ']
    rule, _tmp, *body = toks
    assert _tmp == ':'
    rules[int(rule)] = sorted([list(map(convert_to_type, x)) for x in split(body, '|')], key=len, reverse=False)

# this impl properly backtracks with every possible option (and also solves part 1)
def parse_rest(stack, s):
    while stack and s:
        r, stack = stack[0], stack[1:]
        if isinstance(r, str):
            if r == s[0]:
                s = s[1:]
            else:
                return False
        elif isinstance(r, int):
            for option in rules[r]:
                if parse_rest(option + stack, s):
                    return True
            return False
        else:
            assert False, r
    return not stack and not s

print(sum(1 for m in messages if parse_rest(rules[0][0], m)))
