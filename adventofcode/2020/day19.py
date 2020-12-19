import fileinput
from collections import Counter

def parse():
    rules = {}
    msgs = []
    is_rule = True
    for line in fileinput.input():
        l = line.rstrip()
        if not l:
            is_rule = False
            continue
        if is_rule:
            rule_num,rule = l.split(': ')
            rule = rule.replace('"','')
            rules[int(rule_num)] = rule.split(' | ')
        else:
            msgs.append(l)
    return rules,msgs

def match(s, rules, rule_num, debug_log=False):
    if debug_log: print('check match', s, rule_num)

    if not s:
        if debug_log: print('empty s')
        # return ('', '')
        return None

    rule = rules[rule_num]
    if rule[0] == 'a':
        if s[0] == 'a':
            return ('a', s[1:])
        else:
            return None
    if rule[0] == 'b':
        if s[0] == 'b':
            return ('b', s[1:])
        else:
            return None

    s_copy = str(s)
    rule_nums = [int(r) for r in rule[0].split(' ')]
    matched = ''
    rule_matches = True
    for rn in rule_nums:
        m = match(s_copy, rules, rn, debug_log)
        if not m:
            rule_matches = False
            break
        matched += m[0]
        s_copy = m[1]

    if rule_matches:
        # if debug_log and rule_num == 42: print(s,rule_num,matched,s_copy)
        if debug_log: print(s,rule_num,matched,s_copy)
        return (matched, s_copy)

    if len(rule) == 1:
        return None

    # if we get here, it's | options, and the left option already failed
    # Try the other option
    s_copy = str(s)
    rule_nums = [int(r) for r in rule[1].split(' ')]
    matched = ''
    rule_matches = True
    for rn in rule_nums:
        m = match(s_copy, rules, rn, debug_log)
        if not m:
            rule_matches = False
            break
        matched += m[0]
        s_copy = m[1]

    if rule_matches:
        # if debug_log and rule_num == 42: print(s,rule_num,matched,s_copy)
        if debug_log: print(s,rule_num,matched,s_copy)
        return (matched, s_copy)
    else:
        return None

def part1(rules, msgs):
    total = 0
    for msg in msgs:
        debug_log = False
        # if msg == 'aaaaabbaabaaaaababaa':
        #     debug_log = True
        m = match(msg, rules, 0, debug_log)
        if m and m[1] == '':
            # print('match',msg)
            total += 1
    return total

def match_alt_rule8(s, rules):
    # Alternate rule 8 says: "1 or more of rule 42"
    n = 0
    while True:
        if s == '':
            return ('', n)
        m = match(s, rules, 42)
        if not m:
            return (s, n)
        n += 1
        s = m[1]
    return ('', 0)

def match_alt_rule11(s, rules):
    # Alternate rule 11 says: "N of rule 42, N rule 31; N > 0"
    s_copy = str(s)
    s_copy, rule42_n = match_alt_rule8(s_copy, rules)
    if rule42_n == 0:
        return (s, 0)
    # print(s_copy)

    rule31_n = 0
    while True:
        if s_copy == '' and rule42_n == rule31_n:
            return ('', rule42_n)
        m = match(s_copy, rules, 31)
        if not m:
            # print('(no match)',s_copy)
            return (s,0)
        rule31_n += 1
        s_copy = m[1]
    return None

def matches_alt_rule0(s, rules):
    # apply rule 11 first, to prevent rule8 from eating too much
    n11 = 0
    for i in range(len(s)):
        s_copy = s[i:]
        s_copy,n11 = match_alt_rule11(s_copy, rules)
        if n11 > 0:
            # print("non-0 N",i,s_copy,n11,s[:i])
            if s_copy != '':
                return False
            s = s[:i]
            break
    s,n8 = match_alt_rule8(s, rules)
    return (s == '' and n11 > 0 and n8 > 0)

def part2(rules, msgs):
    total = 0
    for msg in msgs:
        if matches_alt_rule0(msg, rules):
            # print(msg, ': match')
            total += 1
    return total

rules,msgs = parse()
# print(rules)
# print(msgs)

# print(match('aa', rules, 2))
# print(match('bc', rules, 1))

# print(match_alt_rule8('bbaaba', rules))
# print(match_alt_rule8('bbaab', rules))
# print(match_alt_rule8('bbaabbbaabb', rules))
# print(match('bbaba', rules, 31))
# print(match_alt_rule11('bbaabbbaba', rules))
# print(matches_alt_rule0('bbaabbbaba', rules))
# print(matches_alt_rule0('bbaabbbaabbbaba', rules))

# print(match_alt_rule8('aaaaabbaabaaaaababaa', rules))
# print(match_alt_rule11('aaaaabbaabaaaaababaa', rules))
# print(match_alt_rule8('aaaaabbaab', rules))
# print(match('aaaaa', rules, 42))
# print(match('bbaab', rules, 42))
# print(matches_alt_rule0('aaaaabbaabaaaaababaa', rules))

# This one is returning True, should return False
# print(matches_alt_rule0('aaaabbaaaabbaaa', rules))

print(part1(rules,msgs))
print(part2(rules,msgs))
