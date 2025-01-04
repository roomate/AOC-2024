# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:30:50 2024

@author: hugon
"""

import operator
modulo = 16777216

Lines = []
with open('input.txt') as file:
    for line in file:
        Lines += [int(line.rstrip('\n'))]

def prune(secret):
    return secret % modulo

def process(secret):
    tmp = secret*64
    
    secret = operator.xor(tmp, secret)
    secret = prune(secret)
    
    tmp = secret//32
    secret = operator.xor(tmp, secret)        
    secret = prune(secret)    

    tmp = secret*2048
    secret = operator.xor(tmp, secret)
    secret = prune(secret)

    return secret

Output = []
for l in Lines:
    n = l
    for _ in range(2000):
        n = process(n)
    Output += [n]
print(sum(Output))