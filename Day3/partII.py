# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:39:47 2024

@author: hugon
"""
text = ""
with open(r"C:\Users\hugon\OneDrive\Bureau\AOC\Day3\input.txt") as file:
    for line in file:
        text += line

def is_figure(c):
    if c == '0':
        return True
    elif c == '1':
        return True
    elif c == '2':
        return True
    elif c == '3':
        return True
    elif  c == '4':
        return True
    elif c == '5':
        return True
    elif c == '6':
        return True
    elif c == '7':
        return True
    elif c == '8':
        return True
    elif  c == '9':
        return True

def detect_figure(string):
    j = 0
    figure = ''
    while is_figure(string[j]):
        figure += string[j]
        j += 1
    return figure

count = 0
able = True
for i in range(len(text) - 7):
    # print(text[i: i + 15])
    if text[i:i+4] == "do()":
        able = True
    elif text[i:i+7] == "don't()":
        able = False
    if text[i: i + 4] == "mul(" and able:
        figure_1 = detect_figure(text[i+4:])
        j = len(figure_1)
        if text[4 + i + j] == ',' and len(figure_1) != 0:
            j += 1
            figure_2 = detect_figure(text[4 + i + j:])
            j += len(figure_2)
            if text[4 + i + j] == ')' and len(figure_2) != 0:
                count += int(figure_1)*int(figure_2)
print(count)