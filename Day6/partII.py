# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:42:16 2025

@author: hugon
"""
import copy
import time
map_ = []
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day6\input.txt') as file:
    for line in file:
        map_ += [list(line.split()[0])]

for i, line in enumerate(map_):
    for j, s in enumerate(line):
        if s == '^':
            pos = (i,j)
            pos_init = pos

pad = {'^': (-1,0), '>': (0,1), '<': (0,-1), 'v': (1,0)}
p = pad[map_[pos[0]][pos[1]]]
next_pos = (pos[0] + p[0], pos[1] + p[1])
width = len(map_[0])
length = len(map_)

explored = {str(pos) : '^'}

def on_limit(pos):
    if pos[0] < 0 or pos[0] == length:
        return True
    elif pos[1] < 0 or pos[1] == width:
        return True
    else:
        return False

map_c = copy.deepcopy(map_)

while not on_limit(next_pos):
    p = pad[map_c[pos[0]][pos[1]]]
    
    if map_c[next_pos[0]][next_pos[1]] == '.' or map_c[next_pos[0]][next_pos[1]] == 'X':
        map_c[next_pos[0]][next_pos[1]] = map_c[pos[0]][pos[1]]
        map_c[pos[0]][pos[1]] = 'X'
        pos = next_pos
    elif map_c[next_pos[0]][next_pos[1]] == '#':
        if map_c[pos[0]][pos[1]] == '^':
            map_c[pos[0]][pos[1]] = ">"
        elif map_c[pos[0]][pos[1]] == '>':
            map_c[pos[0]][pos[1]] = 'v'
        elif map_c[pos[0]][pos[1]] == 'v':
            map_c[pos[0]][pos[1]] = '<'
        elif map_c[pos[0]][pos[1]] == '<':
            map_c[pos[0]][pos[1]] = '^'
        p = pad[map_c[pos[0]][pos[1]]]
    next_pos = (pos[0] + p[0], pos[1] + p[1])

map_c[pos[0]][pos[1]] = 'X'

def forward(map_test, pos):
    try:
        p = pad[map_test[pos[0]][pos[1]]]
    except KeyError:
        return map_test, pos
    next_pos = (pos[0] + p[0], pos[1] + p[1])
    if on_limit(next_pos):
        return map_test, next_pos
    if map_test[next_pos[0]][next_pos[1]] == '.':
        map_test[next_pos[0]][next_pos[1]] = map_test[pos[0]][pos[1]]
        map_test[pos[0]][pos[1]] = '.'
        pos = next_pos
    elif map_test[next_pos[0]][next_pos[1]] == '#' or map_test[next_pos[0]][next_pos[1]] == 'O':
        if map_test[pos[0]][pos[1]] == '^':
            map_test[pos[0]][pos[1]] = ">"
        elif map_test[pos[0]][pos[1]] == '>':
            map_test[pos[0]][pos[1]] = 'v'
        elif map_test[pos[0]][pos[1]] == 'v':
            map_test[pos[0]][pos[1]] = '<'
        elif map_test[pos[0]][pos[1]] == '<':
            map_test[pos[0]][pos[1]] = '^'

        return map_test, pos

    return map_test, next_pos

def check_loop(map_test, explored, pos):
    while True:
        
        map_test, pos = forward(map_test, pos) #Update the map
        if on_limit(pos):
            return False
        if (str(pos) in explored) and (map_test[pos[0]][pos[1]] in explored[str(pos)]):
            return True
        elif (str(pos) in explored) and (map_test[pos[0]][pos[1]] not in explored[str(pos)]):
            explored[str(pos)] += map_test[pos[0]][pos[1]]
        elif (str(pos) not in explored):
            explored[str(pos)] = map_test[pos[0]][pos[1]]

count = []
t = time.time()
for i, m in enumerate(map_c):
    for j, s in enumerate(m):
        if s == 'X' and (i,j) != pos_init:
            explored = {str(pos_init) : '^'}
            map_test = copy.deepcopy(map_)
            map_test[i][j] = 'O'
            count += [(i,j)] if check_loop(map_test, explored, pos_init) else []
print(len(count))
print(time.time() - t)