# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:43:00 2025

@author: hugon
"""

map_ = []
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day10\input.txt') as file:
    for line in file:
        map_ += [list(line.strip())]

def figure_around(map_, pos, figure, direction):
    figure = str(figure)
    i = pos[0]
    j = pos[1]
    if i - 1 >= 0 and (direction == 'Up' or direction == 'All'):
        if map_[i - 1][j] == figure:
            return True
    if j - 1 >= 0 and (direction == 'Left' or direction == 'All'):
        if map_[i][j - 1] == figure:
            return True
    if i + 1 < len(map_) and (direction == 'Bottom' or direction == 'All'):
        if map_[i + 1][j] == figure:
            return True
    if j + 1 < len(map_[0]) and (direction == 'Right' or direction == 'All'):
        if map_[i][j + 1] == figure:
            return True
    return False
        
def find_head_trails(map_):
    head_trails = []
    for i, line in enumerate(map_):
        for j, k in enumerate(line):
            if k == '0' and figure_around(map_, (i, j), 1, 'All'):
                head_trails += [(i, j)]
    return head_trails

def search(map_, pos, figure):
    output = 0
    if str(figure) == '9':
        return 1
    if figure_around(map_, pos, figure + 1, 'Up'):
        pos_next = (pos[0] - 1, pos[1])
        if str(pos_next) not in visited:
            output += search(map_, pos_next, figure + 1)
        else:
            output += visited[str(pos_next)]
    if figure_around(map_, pos, figure + 1, 'Bottom'):
        pos_next = (pos[0] + 1, pos[1])
        if str(pos_next) not in visited:
            output += search(map_, pos_next, figure + 1)
        else:
            output += visited[str(pos_next)]
    if figure_around(map_, pos, figure + 1, 'Right'):
        pos_next = (pos[0], pos[1] + 1)
        if str(pos_next) not in visited:
            output += search(map_, pos_next, figure + 1)
        else:
            output += visited[str(pos_next)]
    if figure_around(map_, pos, figure + 1, 'Left'):
        pos_next = (pos[0], pos[1] - 1)
        if str(pos_next) not in visited:
            output += search(map_, (pos[0], pos[1] - 1), figure + 1)
        else:
            output += visited[str(pos_next)]
    visited[str(pos)] = output
    return output
   
score = 0 
head_trails = find_head_trails(map_)
for pos in head_trails:
    visited = {}
    score += search(map_, pos, 0)
print(score)