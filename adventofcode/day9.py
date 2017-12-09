with open("day9_input.txt") as f:
    chars = f.read()

# chars = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
# chars = "{{{},{},{{}}}}"
skip = False
depth = 0
score = 0
in_garbage = False
garbage_chars = 0

for c in chars:
    if skip:
        skip = False
    elif in_garbage:
        if c == "!":
            skip = True
        elif c == ">":
            in_garbage = False
        else:
            garbage_chars += 1
    else:
        if c == "{":
            depth += 1
        elif c == "<":
            in_garbage = True
        elif c == "}":
            score += depth
            depth -= 1

print score
print garbage_chars
