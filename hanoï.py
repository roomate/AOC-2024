# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:00:29 2024

@author: hugon
"""

def hanoï(n1, n2, n3):
    count = 0
    if n1[1] + n2[1] + n3[1] == 0: 
        return 0
    
    count += hanoï([n1[0], n1[1] - 1], n3, n2)

    print("Déplacer de {} vers {}".format(n1[0], n3[0]))
    count += 1

    count += hanoï([n2[0], n1[1] - 1], [n1[0], 0], n3)

    return count

n1 = ['A', 3]
n2 = ['B', 0]
n3 = ['C', 0]
hanoï(n1,n2,n3)