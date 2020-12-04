import fileinput
from collections import Counter

def parse():
    passports = []
    p = {}
    for line in fileinput.input():
        keyvals = line.rstrip().split(' ')
        if keyvals[0] == '':
            passports.append(p)
            p = {}
        else:
            for kv in keyvals:
                key, value = kv.split(':')
                p[key] = value
    # Make sure to append the last one!
    if p != {}:
        passports.append(p)
    return passports

def part1(passports):
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    num_valid = 0
    passports_with_required_keys = []
    for p in passports:
        keys = p.keys()
        missing = []
        for r in required:
            if r not in keys:
                missing.append(r)

        if len(missing) == 0:
            num_valid += 1
            passports_with_required_keys.append(p)
        # else:
        #     print('missing', missing, keys)
    return (num_valid, passports_with_required_keys)

def byr_valid(p):
    val = int(p['byr'])
    return (val >= 1920 and val <= 2002)

def iyr_valid(p):
    val = int(p['iyr'])
    return (val >= 2010 and val <= 2020)

def eyr_valid(p):
    val = int(p['eyr'])
    return (val >= 2020 and val <= 2030)

def hgt_valid(p):
    units = p['hgt'][-2:]
    if units == 'cm':
        val = int(p['hgt'][:-2])
        return (val >= 150 and val <= 193)
    elif units == 'in':
        val = int(p['hgt'][:-2])
        return (val >= 59 and val <= 76)
    else:
        return False

def hcl_valid(p):
    val = p['hcl']
    if val[0] != '#':
        return False
    if len(val[1:]) != 6:
        return False
    for c in val[1:]:
        is_digit = (c >= '0' and c <= '9')
        is_hex = (c >= 'a' and c <= 'f')
        if not (is_digit or is_hex):
            return False
    return True

def ecl_valid(p):
    val = p['ecl']
    return val in ['amb','blu','brn','gry','grn','hzl','oth']

def pid_valid(p):
    val = p['pid']
    if len(val) != 9:
        return False
    for c in val:
        is_digit = (c >= '0' and c <= '9')
        if not is_digit:
            return False
    return True

def part2(passports):
    ps_with_req_keys = part1(passports)[1]
    num_valid = 0
    for p in ps_with_req_keys:
        valid = [
            byr_valid(p),
            iyr_valid(p),
            eyr_valid(p),
            hgt_valid(p),
            hcl_valid(p),
            ecl_valid(p),
            pid_valid(p),
        ]
        if all(valid):
            num_valid += 1
        # else:
        #     print(valid)
    return num_valid

passports = parse()
# for p in passports:
#     print(p)
# print(len(passports))

# Wrong: 225
print(part1(passports)[0])
print(part2(passports))
