# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:10:36 2024

@author: hugon
"""
L = []
with open('input.txt', 'r') as file:
    for line in file:
        tmp = line.rstrip('\n').split()
        tmp = [int(i) for i in tmp]
        L += [tmp]

L1 = [L[i][0] for i in range(len(L))]
L2 = [L[i][1] for i in range(len(L))]
L1.sort()
L2.sort()
Output = 0

for i in range(len(L1)):
    Output += abs(L1[i] - L2[i])
print(Output)