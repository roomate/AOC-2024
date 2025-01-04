# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:50:12 2025

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

def swap(L, i, j):
    a = L[i]
    L[i] = L[j]
    L[j] = a
    return L

for s in pages:
    bool_ = True
    for i in range(1,len(s)):
        j = i
        while j >= 1 and s[j] not in occurence[s[j - 1]]:
            s = swap(s, j, j - 1)
            j -= 1
            bool_ = False
    if not bool_:
        middle += int(s[len(s)//2])
print(middle)