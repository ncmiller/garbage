import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(l)
    return vals

def tokenize(s):
    return s.replace('(', '( ').replace(')', ' )').split(' ')

def eval(tokens, add_before_mult):
    # First pass: evaluate paren expressions
    paren_stack = []
    sub_tokens = []
    open_paren_index = -1
    for i in range(len(tokens)):
        token = tokens[i]
        if token == '(':
            if open_paren_index == -1:
                open_paren_index = i
            paren_stack.append(token)
        elif token == ')':
            paren_stack = paren_stack[:-1]
            if not paren_stack:
                sub_tokens.append((open_paren_index, i))
                open_paren_index = -1

    # Evaluate paren expressions, replace in original tokens
    replacements = []
    flat_tokens = list(tokens)
    # print(tokens, sub_tokens)
    for i,j in sub_tokens:
        sub_result = eval(tokens[i+1:j], add_before_mult)
        replacements.append((i,j,sub_result))
    for r in reversed(replacements):
        i,j,value = r
        flat_tokens = flat_tokens[:i] + [value] + flat_tokens[j+1:]

    if add_before_mult:
        # Second pass: Evaluate addition, replace in original tokens
        # print("before_add\n   {}\n   {}".format(tokens,flat_tokens))
        i = 0
        while True:
            if i >= len(flat_tokens):
                break
            if flat_tokens[i] == '+':
                val = int(flat_tokens[i-1]) + int(flat_tokens[i+1])
                if len(flat_tokens) > 3:
                    flat_tokens = flat_tokens[:i-1] + [str(val)] + flat_tokens[i+2:]
                else:
                    return val
                i = 0
            else:
                i += 1

    # print("flat\n   {}\n   {}".format(tokens,flat_tokens))

    # Final pass: evaluate flat tokens left to right
    result = None
    for i in range(len(flat_tokens)):
        token = flat_tokens[i]
        if token == '(':
            assert(False)
        elif token == ')':
            assert(False)
        elif token == '+':
            assert(not add_before_mult)
            if not result:
                result = int(flat_tokens[i-1])
            b = int(flat_tokens[i+1])
            result = (result + b)
        elif token == '*':
            if not result:
                result = int(flat_tokens[i-1])
            b = int(flat_tokens[i+1])
            result = (result * b)
    # print('eval result',tokens,result)
    return result

def find_sub_expressions(expr):
    # list of (start_index, end_index), inclusive
    sub_expressions = []
    return sub_expressions

def part1(vals):
    total = 0
    for line in vals:
        answer = eval(tokenize(line), False)
        # print(line,'=',answer)
        total += answer
    return total

def part2(vals):
    total = 0
    for line in vals:
        answer = eval(tokenize(line), True)
        # print(line,'=',answer)
        total += answer
    return total

vals = parse()
print(part1(list(vals)))
print(part2(list(vals)))
