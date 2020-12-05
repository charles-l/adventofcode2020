import re
with open('input_day4', 'r') as f:
    lines = f.readlines()

required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

num_valid = 0
cur_passport = {}
for l in lines:
    l = l.strip()
    if l == '':
        if set(cur_passport.keys()).issuperset(required_keys):
            byr_valid = 1920 <= int(cur_passport['byr']) <= 2002
            iyr_valid = 2010 <= int(cur_passport['iyr']) <= 2020
            eyr_valid = 2020 <= int(cur_passport['eyr']) <= 2030
            hgt_match = re.fullmatch(r'(\d+)(cm|in)', cur_passport['hgt'])
            if hgt_match and hgt_match.group(2) == 'cm':
                hgt_valid = 150 <= int(hgt_match.group(1)) <= 193
            elif hgt_match and hgt_match.group(2) == 'in':
                hgt_valid = 59 <= int(hgt_match.group(1)) <= 76
            else:
                hgt_valid = False
            hcl_valid = re.fullmatch(r'#[0-9a-f]{6}', cur_passport['hcl'])
            ecl_valid = cur_passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
            pid_valid = re.fullmatch(r'[0-9]{9}', cur_passport['pid'])
            print(dict(zip(("byr_valid", "iyr_valid", "eyr_valid", "hgt_valid", "hcl_valid", "ecl_valid", "pid_valid"), (byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid))))
            if all((byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid)):
                num_valid += 1
        cur_passport = {}
        continue
    print(l.split(' '))
    cur_passport = {**cur_passport,
                    **{x.split(':')[0]: x.split(':')[1] for x in l.split(' ')}}

print(num_valid)
