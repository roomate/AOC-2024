# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:25:26 2024

@author: hugon
"""

left = []
right = []
with open('input.txt', 'r') as file:
    for line in file:
        tmp = line.rstrip('\n').split()
        left += [tmp[0]]
        right += [tmp[1]]

figures = {}
for i in left:
    count = 0
    if i in figures:
        count += figures[i]
    else:
        for j in right:
            if i == j:
                count += 1
        figures[i] = count

count_total = 0
for i in figures:
    count_total += int(i)*figures[i]
print(count_total)