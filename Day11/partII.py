# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:12:18 2025

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
        self.explored = {}
    
    def one_blink(self, figure, count):
        if count == 0:
            return 1
        if figure + ',' + str(count) in self.explored:
            return self.explored[figure + ',' + str(count)]
        if figure == '0':
            output = self.one_blink('1', count - 1)
        elif len(figure)%2 == 0:
            output = self.one_blink(figure[:len(figure)//2], count - 1) + self.one_blink(str(int(figure[len(figure)//2:])), count - 1)
        else:
            output = self.one_blink(str(int(figure)*2024), count - 1)
        self.explored[figure + ',' + str(count)] = output
        return output
        
stone = Stone(line)
out = 0
for s in stone.puzzle:
    out += stone.one_blink(s, 75)
print(out)