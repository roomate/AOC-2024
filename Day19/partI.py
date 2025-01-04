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
    

def recur(towels, design):
    if len(design) == 0:
        return True
    for i in towels:
        if is_prefix(i,design):
            if recur(towels,design[len(i):]):
                return True
    return False

count = 0
for i, towel in enumerate(towels):
    towels[i] = 'X'
    if not recur(towels, towel):
        towels[i] = towel

towels.sort(reverse = True)
print(towels)
for d in designs:
    if recur(towels, d): count += 1

print(count)