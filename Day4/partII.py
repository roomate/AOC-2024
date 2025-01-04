# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 14:49:21 2025

@author: hugon
"""
board = []
with open(r"C:\Users\hugon\OneDrive\Bureau\AOC\Day4\input.txt", 'r') as file:
    for line in file:
        board += line.rsplit()
        
def check_diagonal(board, i, j, direction):
    k = 0
    if direction == 'Left':
        if board[i - 1][j - 1] == 'M' and board[i + 1][j + 1] == 'S':
            k += 1
            return True
        elif board[i - 1][j - 1] == "S" and board[i + 1][j + 1] == "M":
            k += 1
            return True
        else:
            return False
    elif direction == "Right":
        if board[i + 1][j - 1] == 'M' and board[i - 1][j + 1] == 'S':
            k += 1
            return True
        elif board[i + 1][j - 1] == "S" and board[i - 1][j + 1] == "M":
            k += 1
            return True
        else:
            return False

if __name__ == "__main__":
    count = 0
    width = len(board)
    length = len(board[0])
    for i in range(1,len(board) - 1):
        for j in range(1, len(board[0]) - 1):
            if board[i][j] == 'A':
                k = 1 if check_diagonal(board, i, j, "Right") else 0
                k += 1 if check_diagonal(board, i, j, "Left") else 0
                count += 1 if k == 2 else 0
    print(count)