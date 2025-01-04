# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:46:26 2025

@author: hugon
"""

map_ = []
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day6\input.txt') as file:
    for line in file:
        map_ += [list(line.split()[0])]

for i, line in enumerate(map_):
    for j, s in enumerate(line):
        if s == '^':
            pos = (i,j)

pad = {'^': (-1,0), '>': (0,1), '<': (0,-1), 'v': (1,0)}
p = pad[map_[pos[0]][pos[1]]]
next_pos = (pos[0] + p[0], pos[1] + p[1])
width = len(map_[0])
length = len(map_)

def on_limit(pos):
    if pos[0] < 0 or pos[0] == length:
        return True
    elif pos[1] < 0 or pos[1] == width:
        return True
    else:
        return False

print('\n')

while not on_limit(next_pos):
    p = pad[map_[pos[0]][pos[1]]]
    if map_[next_pos[0]][next_pos[1]] == '.' or map_[next_pos[0]][next_pos[1]] == 'X':
        map_[next_pos[0]][next_pos[1]] = map_[pos[0]][pos[1]]
        map_[pos[0]][pos[1]] = 'X'
        pos = next_pos
    elif map_[next_pos[0]][next_pos[1]] == '#':
        if map_[pos[0]][pos[1]] == '^':
            map_[pos[0]][pos[1]] = ">"
        elif map_[pos[0]][pos[1]] == '>':
            map_[pos[0]][pos[1]] = 'v'
        elif map_[pos[0]][pos[1]] == 'v':
            map_[pos[0]][pos[1]] = '<'
        elif map_[pos[0]][pos[1]] == '<':
            map_[pos[0]][pos[1]] = '^'
        p = pad[map_[pos[0]][pos[1]]]
    next_pos = (pos[0] + p[0], pos[1] + p[1])

    
count = 1
for m in map_:
    for l in m:
        if l == 'X':
            count += 1
print(count)