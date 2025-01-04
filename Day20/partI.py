# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:01:47 2024

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

path = {str(S[0]) + ',' + str(S[1]): 0}
count = 0

def find_path(List, S, E, path, count):
    direction = [[-1,0], [1,0], [0,1], [0,-1]]
    for d in direction:
        new_point = (S[0] + d[0], S[1] + d[1])
        if is_possible(len(List[0]), len(List), new_point):
            key_new_point = str(S[0] + d[0]) + ',' + str(S[1] + d[1])
            if List[new_point[0]][new_point[1]] == "." and key_new_point not in path:
                count += 1
                path[str(new_point[0]) + ',' + str(new_point[1])] = count
                find_path(List, new_point, E, path, count)
            if (new_point == E):
                count += 1
                key_E = str(E[0]) + ',' + str(E[1])
                path[key_E] = count
                return path

def find_cheat(List, path):
    """

    Parameters
    ----------
    List : 2D array.
    point : tuple of int

    Returns
    -------
    The coordinates of the point at where you can jump from all points
    on the path.
    """
    direction = [[-1,0], [1,0], [0,1], [0,-1]]
    cheat = []
    for key in path:
        key = key.split(',')
        x = int(key[0])
        y = int(key[1])
        
        key_coord = str(x) + ',' + str(y)
        
        for d in direction:
            new_x = x + d[0]
            new_y = y + d[1]
            
            new_xx = x + 2*d[0]
            new_yy = y + 2*d[1]
            key_new_coord = str(new_xx) + ',' + str(new_yy)
            
            if is_possible(len(List[0]), len(List), (new_xx, new_yy)):
                if List[new_x][new_y] == "#" and List[new_xx][new_yy] != "#" and path[key_new_coord] > path[key_coord]:
                    cheat += [[key_coord, key_new_coord]]
    return cheat

find_path(L, S, E, path, count)
cheat = find_cheat(L, path)

picos_saved = []
output = 0
for c in cheat:
    if path[c[1]] - path[c[0]] > 100:
        output += 1
print(output)    