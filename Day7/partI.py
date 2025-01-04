# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:44:26 2025

@author: hugon
"""

def list_operator(nb):
    if nb == 1:
        return ['+', '*']
    l = list_operator(nb - 1)
    output = []
    for s in l:
        output += [s + '+', s + '*']
    return output
    
argument = []
result = []
with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day7\input.txt') as file:
    for line in file:
        l = line.split(':')
        argument += [l[1].strip().split(' ')]
        result += [l[0].strip()]
        
def fct_operation(string, a, b):
    if string == '*':
        return int(a)*int(b)
    elif string == '+':
        return int(a)+int(b)
    else:
        raise ValueError('There is an error. string is not conform.')

def list_operation(list_op, arg):
    if len(list_op) != len(arg) - 1:
        raise ValueError("Lengths do not match.")
    output = arg[0]
    for i, op in enumerate(list_op):
        output = fct_operation(op, output, arg[i+1])
    return output

count = 0
for i, arg in enumerate(argument):
    nb = len(arg)
    operations = list_operator(nb - 1)
    for j, operation in enumerate(operations):
      figure = list_operation(operation, arg)
      if figure == int(result[i]):
          count += figure
          break
print(count)