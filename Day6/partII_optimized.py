# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:03:37 2025

@author: hugon
"""

import copy
import time
map_ = []
map_c = []
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day6\input.txt') as file:
    for line in file:
        s = line.split()[0]
        map_ += [list(s)]
        map_c += [list(s)]

for i, line in enumerate(map_):
    for j, s in enumerate(line):
        if s == '^':
            pos = (i,j)
            pos_init = pos

pad = {'^': (-1,0), '>': (0,1), '<': (0,-1), 'v': (1,0)}
p = pad[map_[pos[0]][pos[1]]]
next_pos = (pos[0] + p[0], pos[1] + p[1])
head = '^'

width = len(map_[0])
length = len(map_)

explored = {str(pos) : head}

def on_limit(pos):
    if pos[0] < 0 or pos[0] == length:
        return True
    elif pos[1] < 0 or pos[1] == width:
        return True
    else:
        return False

path = []

while not on_limit(next_pos):
    if map_[next_pos[0]][next_pos[1]] == '.':
        if next_pos not in path:
            path += [next_pos]
        pos = next_pos
    elif map_c[next_pos[0]][next_pos[1]] == '#':
        if head == '^':
            head = ">"
        elif head == '>':
            head = 'v'
        elif head == 'v':
            head = '<'
        elif head == '<':
            head = '^'
        p = pad[head]
    next_pos = (pos[0] + p[0], pos[1] + p[1])

def forward(map_test, pos, head):
    try:
        p = pad[head]
    except KeyError:
        return head, pos
    next_pos = (pos[0] + p[0], pos[1] + p[1])
    if on_limit(next_pos):
        return head, next_pos
    if map_test[next_pos[0]][next_pos[1]] == '.':
        pos = next_pos
    elif map_test[next_pos[0]][next_pos[1]] == '#' or map_test[next_pos[0]][next_pos[1]] == 'O':
        if head == '^':
            head = ">"
        elif head == '>':
            head = 'v'
        elif head == 'v':
            head = '<'
        elif head == '<':
            head = '^'

        return head, pos

    return head, next_pos

def check_loop(map_test, explored, pos, head):
    while True:
        head, pos = forward(map_test, pos, head) #Update the map
        if on_limit(pos):
            return False
        if (str(pos) in explored) and (head in explored[str(pos)]):
            return True
        elif (str(pos) in explored) and (map_test[pos[0]][pos[1]] not in explored[str(pos)]):
            explored[str(pos)] += head
        elif (str(pos) not in explored):
            explored[str(pos)] = head

count2 = []
head = '^'
t = time.time()
for X in path:
    explored = {str(pos_init) : '^'}
    map_[X[0]][X[1]] = 'O'
    count2 += [X] if check_loop(map_, explored, pos_init, head) else []
    map_[X[0]][X[1]] = '.'
print(len(count2))
print(time.time() - t)