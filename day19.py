from boltons.iterutils import split
import re
with open('input_day19') as f:
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
    rules[int(rule)] = [list(map(convert_to_type, x)) for x in split(body, '|')]

def check_string(msg):
    def f(rule_id, s):
        for option in rules[rule_id]:
            s1 = s  # reset the string for this option
            for x in option:
                if isinstance(x, int):
                    matched, rest = f(x, s1)
                    if not matched:
                        break
                    else:
                        s1 = rest
                elif isinstance(x, str):
                    if not s1 or s1[0] != x:
                        break
                    s1 = s1[1:]
            else:
                return True, s1
        return False, s

    res, rest = f(0, msg)
    if res:
        return not rest
    else:
        return False

print(sum(1 for m in messages if check_string(m)))
