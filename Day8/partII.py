# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:13:10 2025

@author: hugon

To do part II, you remove the while True conditions and fix k = 2.
"""

map_ = []
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day8\input.txt') as file:
    for line in file:
        map_ += [list(line.strip())]

length = len(map_)
width = len(map_[0])

def is_inside(loc):
    if loc[0] < 0 or loc[0] >= length:
        return False
    elif loc[1] < 0 or loc[1] >= width:
        return False
    return True

#Dictionary for the locations of the antennas
locations = {}

#Store the antinodes' location
antinode = {}

for i, line in enumerate(map_):
    for j, s in enumerate(line):
        if s != '.':
            if s not in locations:
                locations[s] = [(i,j)]
            else:
                locations[s] += [(i,j)]

for key in locations:
    loc = locations[key]
    for i, l in enumerate(loc):
        for j in range(i + 1, len(loc)):
            k = 0
            while True:
                antinode_1 = (k*(loc[j][0] - l[0]) + l[0], k*(loc[j][1] - l[1]) + l[1])
                if not is_inside(antinode_1):
                    break
                else:
                    if antinode_1 not in antinode:
                        antinode[antinode_1] = 0
                k += 1
            k = 0
            while True:
                antinode_2 = (k*(l[0] - loc[j][0]) + loc[j][0], k*(l[1] - loc[j][1]) + loc[j][1])
                if not is_inside(antinode_2):
                    break
                else:
                    if antinode_2 not in antinode:
                        antinode[antinode_2] = 0
                k += 1
print(len(antinode))