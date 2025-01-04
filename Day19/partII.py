towels = None
designs = []
with open("./input.txt") as f:
    for line in f:
        if towels is None:
            towels= line.strip().split(', ')
        elif line.strip() != "":
            designs += [line.strip()]

def is_prefix(towel, design):
    if (len(towel) > len(design)): return False
    return design[:len(towel)] == towel
    
dicti = {}

def recur(towels, design):
    n = 0
    if len(design) == 0:
        return 1
    if design in dicti:
        return dicti[design]
    for i in towels:
        if is_prefix(i,design):
            n += recur(towels,design[len(i):])
    dicti[design] = n
    return n

count = 0

for d in designs:
    print(count)
    count += recur(towels, d)
print(count)