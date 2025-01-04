# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:33:49 2024

@author: hugon
"""
input_ = []
with open(r"\Users\hugon\OneDrive\Bureau\AOC\Day2\input.txt") as file:
    for line in file:
        input_ += [line.rsplit()]

solution = []
with open(r"\Users\hugon\OneDrive\Bureau\AOC\Day2\file.txt") as file:
    for line in file:
        line = line.rsplit()
        if line[0] == 'true':
            solution += [True]
        else:
            solution += [False]

def check_safety(line, j):
    L = line.copy()
    if j is not None:
        del L[j]
    increas = int(L[1]) - int(L[0]) >= 0
    for i in range(1, len(L)):
        a = int(L[i])
        b = int(L[i - 1])
        test = a>=b
        if test != increas or a == b or abs(a - b) > 3:
            return False
    return True

if __name__ == '__main__':   
    count = 0
    for i, line in enumerate(input_):
        increas = int(line[1]) - int(line[0]) >= 0
        safe = check_safety(line, None)
        if safe: count += 1
        if not safe:
            for j in range(len(line)):
                if check_safety(line, j):
                    count += 1
                    break
    print(count)