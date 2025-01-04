# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:30:50 2024

@author: hugon
"""
import matplotlib.pyplot as plt
import operator
import numpy as np
modulo = 16777216

Lines = []
with open('input.txt') as file:
    for line in file:
        Lines += [line.rstrip('\n')]

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

    return str(secret)

order = {}

for i, l in enumerate(Lines):
    n = process(int(l))
    Price = int(n[-1])
    returns = [np.NAN]
    visited = {}
    for j in range(1,2000):
        n = process(int(n))
        prev_price = Price
        Price = int(n[-1])
        returns += [Price - prev_price]
        if j >= 4:
            key = str(returns[j - 3]) + str(returns[j - 2]) + str(returns[j - 1]) + str(returns[j])
            if key in order and key not in visited:
                order[key] += Price
            elif key not in order:
                order[key] = Price
            visited[key] = 1
print(max(order.values()))