# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:57:41 2025

@author: hugon
"""

line = []

with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day11\input.txt') as file:
    for l in file:
        line += l.split(" ")
print(line)
class Stone:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    
    def one_blink(self):
        output= []
        for i, stone in enumerate(self.puzzle):
            if stone == '0':
                output += ['1']
            elif len(stone)%2 == 0:
                output += [stone[:len(stone)//2]] + [str(int(stone[len(stone)//2:]))]
            else:
                output += [str(int(stone)*2024)]
        self.puzzle = output
        
stone = Stone(line)
for _ in range(25):
    stone.one_blink()
print(len(stone.puzzle))