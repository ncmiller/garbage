from collections import defaultdict
from operator import *

compops = {
    ">" : gt,
    "<" : lt,
    "<=" : le,
    ">=" : ge,
    "==" : eq,
    "!=" : ne,
}

incops = {
    "inc" : add,
    "dec" : sub,
}

"""read lines from stdin, split lines on whitespace"""
import fileinput
ops = []
registers = defaultdict(int)
overall_max= -1
for line in fileinput.input():
    reg, incop, val, _, regcond, regop, regval = line.split()
    val = int(val)
    regval = int(regval)
    regop = compops[regop]
    incop = incops[incop]
    if regop(registers[regcond], regval):
        registers[reg] = incop(registers[reg], val)
    overall_max = max(registers.values() + [overall_max])

print max(registers.values())
print overall_max


