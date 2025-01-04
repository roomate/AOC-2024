# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:13:07 2024

@author: hugon
"""
codes = []
numeric_pad = {'0': (1,0), '1': (0,1), '2': (1,1), '3': (2,1), '4': (0,2), '5': (1,2), '6': (2,2)
           , '7': (0,3), '8': (1,3), '9': (2,3), 'A': (2,0)}

key_pad = {'<': (0,0), '^': (1,1), 'v': (1,0), '>': (2,0), 'A': (2,1)}

with open(r"\Users\hugon\OneDrive\Bureau\AOC\Day21\input.txt") as file:
    for line in file:
        codes += line.rsplit()

def numeric_to_pad(num_1, num_2):
    number_1 = numeric_pad[num_1]
    number_2 = numeric_pad[num_2]
    out = []
    diff = [number_2[0] - number_1[0], number_2[1] - number_1[1]]
    if diff[0] > 0 and diff[1] > 0: #Go Up and Right
        out += ['>'*diff[0] + '^'*diff[1] + 'A']
        if diff[0] != 0 and diff[1] != 0:
            out += ['^'*diff[1] + '>'*diff[0] + 'A']
    elif diff[0] <= 0 and diff[1] > 0: #Go Left and Up
        out += ['^'*diff[1] + '<'*abs(diff[0]) + 'A']
        if (number_1[1] != 0 or number_2[0] != 0):
            if diff[0] != 0 and diff[1] != 0:
                out += ['<'*abs(diff[0]) + '^'*diff[1] + 'A']
    elif diff[0] <= 0  and diff[1] <= 0: #Go Left and Down
        out += ['<'*abs(diff[0]) + 'v'*abs(diff[1]) + 'A']
        if diff[0] != 0 and diff[1] != 0:
            out += ['v'*abs(diff[1]) + '<'*abs(diff[0]) + 'A'] 
    elif diff[0] > 0 and diff[1] <= 0: #Go Rigt and Down
        out += ['>'*diff[0] + 'v'*abs(diff[1]) + 'A']
        if number_2[1] != 0 or number_1[0] != 0:
            if diff[0] != 0 and diff[1] != 0:
                out += ['v'*abs(diff[1]) + '>'*diff[0] + 'A']
    return out


def pad_to_pad(s1, s2):
    """
    The output is a list
    """
    symbol_2 = key_pad[s2]
    symbol_1 = key_pad[s1]
    out = []
    diff = [symbol_2[0] - symbol_1[0], symbol_2[1] - symbol_1[1]]
    if diff[0] > 0 and diff[1] > 0: #Go Up and Right
        out += ['>'*diff[0] + '^'*diff[1] + 'A']
        if symbol_1[0] == 1: #To avoid the forbidden case
                out += ['^'*diff[1] + '>'*diff[0] + 'A']
    elif diff[0] <= 0 and diff[1] > 0: #Go Left and Up
        out += ['^'*diff[1] + '<'*abs(diff[0]) + 'A']
        if diff[0] != 0:
            out += ['<'*abs(diff[0]) + '^'*diff[1] + 'A']
    elif diff[0] <= 0  and diff[1] <= 0: #Go Left and Down
        out += ['v'*abs(diff[1]) + '<'*abs(diff[0]) + 'A']
        if symbol_1[0] != 1 and abs(diff[0]) == 1: #To avoid the forbidden case
            out += ['<' + 'v' + 'A']
    elif diff[0] > 0 and diff[1] <= 0: #Go Rigt and Down
        out += ['>'*diff[0] + 'v'*abs(diff[1]) + 'A']
        if diff[1] != 0:
            out += ['v'*abs(diff[1]) + '>'*diff[0] + 'A']
    return out

def build_code(s1, s2, nb_robot):
    if nb_robot == 0:
        return [s1 + s2]
    Output = []
    code = pad_to_pad(s1,s2)
    code = ['A' + l for l in code]
    for piece_code in code:
        tmp = []
        for i in range(1,len(piece_code)):
            tmp += build_code(piece_code[i - 1], piece_code[i], nb_robot - 1)
    Output += [tmp]
    return Output

dicti = {}
def build_code_count(s1, s2, nb_robot):
    if nb_robot == 0:
        return 1
    if s1 + s2 + str(nb_robot) in dicti:
        return dicti[s1 + s2 + str(nb_robot)]
    Output = []
    code = pad_to_pad(s1, s2)
    code = ['A' + l for l in code]
    for piece_code in code: 
        #If two possibilities
        tmp = 0
        for i in range(1,len(piece_code)):
            tmp += build_code_count(piece_code[i - 1], piece_code[i], nb_robot - 1)
        Output += [tmp]
    dicti[s1 + s2 + str(nb_robot)] = min(Output)
    return min(Output)

nb_robot = 25
key_codes = []
for i, code in enumerate(codes):
    code = 'A' + code
    pad_code = []
    for j in range(1,len(code)):
        pad_code += [numeric_to_pad(code[j - 1], code[j])]
    key_codes += [pad_code]

message_coded = []

count = []
for i, key_code in enumerate(key_codes):
    count_i = 0
    for element in key_code:
        Output = []
        for string in element:
            string = 'A' + string
            tmp = 0
            for j in range(1,len(string)):
                tmp += build_code_count(string[j - 1], string[j], nb_robot)
            Output += [tmp]
        count_i += min(Output)
    count += [count_i*int(codes[i][:3])]
print(sum(count))