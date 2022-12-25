import fileinput

def snafu_to_dec(s):
    dec = 0
    slen = len(s)
    for digit_i in range(len(s)):
        digit = s[digit_i]
        exp = slen - digit_i - 1
        if digit >= '0' and digit <= '2':
            dec += (int(digit) * 5**exp)
        elif digit == '-':
            dec -= (5**exp)
        elif digit == '=':
            dec -= (2 * 5**exp)
    return dec

def target_diff(target, exp, snafu_digit):
    if snafu_digit >= '0' and snafu_digit <= '2':
        ord_digit = ord(snafu_digit) - ord('0')
    elif snafu_digit == '-':
        ord_digit = -1
    elif snafu_digit == '=':
        ord_digit = -2
    return target - ord_digit * 5 ** exp

def dec_to_snafu(d):
    digit_i = 1
    while True:
        if 2 * 5**digit_i - 1 >= d:
            break
        digit_i += 1
    num_digits = digit_i + 1
    s = ['0' for _ in range(num_digits)]

    target = d
    options = ['0','1','2','-','=']
    for i in range(num_digits):
        best_option = None
        best_diff = 10000000000000000
        for o in options:
            diff = target_diff(target, num_digits - i - 1, o)
            if abs(diff) < abs(best_diff):
                best_diff = diff
                best_option = o
        s[i] = best_option
        target = best_diff

    return ''.join(s)

lines = [line.rstrip() for line in fileinput.input()]
total = sum([snafu_to_dec(s) for s in lines])
print(total)
print(dec_to_snafu(total))
