import sys

def parse_range(range_str):
    rs = range_str.split('-')
    return (int(rs[0]), int(rs[1]))

def parse():
    lines = [l.rstrip() for l in sys.stdin.readlines()]
    line_no = 0

    rules = []
    while True:
        l = lines[line_no]
        if not l:
            break
        name,ranges_str = l.split(': ')
        rs_str = ranges_str.split(' ')
        rs = (parse_range(rs_str[0]), parse_range(rs_str[2]))
        rules.append((name, rs))
        line_no += 1

    line_no += 2 # skip newline and the line that says "your ticket:"
    my_ticket = [int(field) for field in lines[line_no].split(',')]

    line_no += 3 # skip newlines and the line that says "nearby tickets:"
    nearby_tickets = []
    for i in range(line_no, len(lines)):
        nearby_tickets.append([int(field) for field in lines[i].split(',')])

    return rules,my_ticket,nearby_tickets

def matches_any_rule(field, rules):
    for rule in rules:
        name,ranges = rule
        r1_lo,r1_hi = ranges[0]
        r2_lo,r2_hi = ranges[1]
        if field >= r1_lo and field <= r1_hi:
            return True
        if field >= r2_lo and field <= r2_hi:
            return True
    return False

def find_invalid_fields(ticket, rules):
    invalid_fields = []
    for field in ticket:
        if not matches_any_rule(field, rules):
            invalid_fields.append(field)
    return invalid_fields

def part1(vals):
    rules, my_ticket, nearby_tickets = vals
    sum_invalid = 0
    for ticket in nearby_tickets:
        invalid_fields = find_invalid_fields(ticket, rules)
        sum_invalid += sum(invalid_fields)
        # print(ticket, invalid_fields)
    return sum_invalid

def in_range(field, ranges):
    r1_lo,r1_hi = ranges[0]
    r2_lo,r2_hi = ranges[1]
    if field >= r1_lo and field <= r1_hi:
        return True
    if field >= r2_lo and field <= r2_hi:
        return True
    return False


def find_candidate_rules(field_index, rules, nearby_tickets):
    values = [t[field_index] for t in nearby_tickets]
    candidate_rules = set(rules)
    for v in values:
        # print(len(candidate_rules))
        matching_rules = set()
        for r in candidate_rules:
            if in_range(v, r[1]):
                matching_rules.add(r)
        candidate_rules = candidate_rules.intersection(matching_rules)
    return candidate_rules

def part2(vals):
    rules, my_ticket, nearby_tickets = vals
    valid_tickets = []
    for ticket in nearby_tickets:
        invalid_fields = find_invalid_fields(ticket, rules)
        if not invalid_fields:
            valid_tickets.append(ticket)
    remaining_rules = set(rules)

    # print(valid_tickets)

    field_matches = {}
    nfields = len(my_ticket)
    unresolved_fields = set([i for i in range(nfields)])
    while unresolved_fields:
        # print('---- {} unresolved fields ----'.format(len(unresolved_fields)))
        for field_index in range(nfields):
            if field_index not in unresolved_fields:
                continue
            candidates = find_candidate_rules(field_index, remaining_rules, valid_tickets)
            if len(candidates) == 1:
                c = list(candidates)[0]
                # print('[{}] matched rule {}'.format(field_index, c))
                field_matches[field_index] = c
                remaining_rules.remove(c)
                unresolved_fields.remove(field_index)
            elif len(candidates) == 0:
                assert(False)
            # else:
                # print('[{}] {} candidates'.format(field_index, len(candidates)))

    # print(field_matches)
    product = 1
    for i in range(nfields):
        if 'departure' in field_matches[i][0]:
            # print(i, my_ticket[i], field_matches[i][0])
            product *= my_ticket[i]

    return product

vals = parse()
# print(vals)
# print(len(vals))
print(part1(list(vals)))
print(part2(list(vals)))
