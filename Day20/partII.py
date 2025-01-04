# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:54:50 2024

@author: hugon
"""

import sys

sys.setrecursionlimit (100000)

L = []
with open('input.txt', 'r') as file:
    for line in file:
        tmp = line.rstrip('\n')
        L += [tmp]

for i, line in enumerate(L):
    for j, c in enumerate(line):
        if c == 'S':
            S = (i,j)
        elif c == 'E':
            E = (i,j)


def is_possible(width, length, new_point):
    if (0 > new_point[1] or new_point[1] >= width): return False
    elif (0 > new_point[0] or new_point[0] >= length): return False
    return True

direction = [[-1,0], [1,0], [0,1], [0,-1]]

def convert_to_key(position):
    return str(position[0]) + ',' + str(position[1])

path = {convert_to_key(S): 0}

def find_path(List, S, E, path, count):
    for d in direction:
        new_point = (S[0] + d[0], S[1] + d[1])
        if is_possible(len(List[0]), len(List), new_point):
            key_new_point = convert_to_key(new_point)
            if List[new_point[0]][new_point[1]] == "." and key_new_point not in path:
                count += 1
                path[key_new_point] = count
                find_path(List, new_point, E, path, count)
            if (new_point == E):
                count += 1
                key_E = convert_to_key(E)
                path[key_E] = count
                return path
            
def modify(L, st, i):
    return L[:i] + st + L[i + 1:]

def display(L):
    for l in L:
        print(l)

def find_jump_cheat(path, position, cheat):
    position_t = position.split(",")
    x = int(position_t[0])
    y = int(position_t[1])
    for key in path:
        key = key.split(',')
        i = int(key[0])
        j = int(key[1])
        if abs(x - i) + abs(y - j) <= 20 and abs(x - i) + abs(y - j) > 0: 
            key_new_point = convert_to_key((i,j))
            if path[key_new_point] > path[position]:
                cheat[position, str(i) + ',' + str(j)] = abs(x - i) + abs(y - j)

import numpy as np
count = 0
find_path(L, S, E, path, count)

cheat = {}
for pos_init in path:
    find_jump_cheat(path, pos_init, cheat)

saved = []

for key in cheat:
    pos_init = key[0] #Position before jump
    pos_fin = key[1] #Position after jump
    nitro = cheat[key] #nitro saved after jumping
    value_init = path[pos_init] #initial value
    value_fin = path[pos_fin] #Final value
    saved += [value_fin - value_init - nitro]

print(len(np.where(np.array(saved) >= 100)[0]))