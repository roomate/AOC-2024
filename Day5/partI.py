# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 17:50:35 2025

@author: hugon
"""

instructions = []
pages = []
after = False
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day5\input.txt') as file:
    for line in file:
        if line == '\n':
            after = True
        elif not after:
            line = line.replace("\n", "")
            instructions += [line.rsplit('|')]
        else:
            line = line.replace("\n", "")
            pages += [line.rsplit(',')]

occurence = {}
for inst in instructions:
    if inst[0] not in occurence:
        occurence[inst[0]] = [inst[1]]
    else:
        occurence[inst[0]] += [inst[1]]
    if inst[1] not in occurence:
        occurence[inst[1]] = []
middle = 0
for s in pages:
    bool_ = True
    for i, l in enumerate(s):
        for j in range(i + 1, len(s)):
            if s[j] not in occurence[l]:
                bool_ = False
                break
        if bool_ == False:
            break
    if bool_:
        middle += int(s[len(s)//2])
print(middle)
