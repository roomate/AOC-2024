# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:00:45 2024

@author: hugon
"""

board = []
with open(r"C:\Users\hugon\OneDrive\Bureau\AOC\Day4\input.txt", 'r') as file:
    for line in file:
        board += line.rsplit()

def check_diagonal(board, i, j, direction):
    if direction == 'Up_Left':
        if i - 3 < 0 or j - 3 < 0:
            return False
        if board[i - 1][j - 1] == 'M' and board[i - 2][j - 2] == 'A' and board[i - 3][j - 3] == 'S':
            return True
        else:
            return False
    elif direction == 'Up_Right':
        if i - 3 < 0 or j + 3 >= len(board[0]):
            return False
        if board[i - 1][j + 1] == 'M' and board[i - 2][j + 2] == 'A' and board[i - 3][j + 3] == 'S':
            return True
        else:
            return False
    elif direction == 'Down_Right':
        if i + 3 >= len(board) or j + 3 >= len(board[0]):
            return False
        if board[i + 1][j + 1] == 'M' and board[i + 2][j + 2] == 'A' and board[i + 3][j + 3] == 'S':
            return True
        else:
            return False
    elif direction == 'Down_Left':
        if i + 3 >= len(board) or j - 3 < 0:
            return False
        if board[i + 1][j - 1] == 'M' and board[i + 2][j - 2] == 'A' and board[i + 3][j - 3] == 'S':
            return True
        else:
            return False
        
def check_vertical(board, i, j, direction):
    if direction == 'Down':
        if i + 3 >= len(board):
            return False
        if board[i + 1][j] == "M" and board[i + 2][j] == "A" and board[i + 3][j] == "S":
            return True
        else:
            return False
    elif direction == "Up":
        if i - 3 < 0:
            return 
        if board[i - 3][j] == "S" and board[i -  2][j] == "A" and board[i - 1][j] == "M":
            return True
        else:
            return False
    else:
        print("Error, direction not valid.")
        return False

def check_horizontal(board, i, j, direction):
    if direction == 'Right':
        if j + 3 >= len(board[0]):
            return False
        if board[i][j + 1] == "M" and board[i][j + 2] == 'A' and board[i][j + 3] == 'S':
            return True
        else:
            return False
    elif direction == "Left":
        if j - 3 < 0:
            return False
        if board[i][j - 3] == "S" and board[i][j - 2] == 'A' and board[i][j - 1] == 'M':
            return True
        else:
            return False
    else:
        print("Error, direction not valid.")
        return False

if __name__ == "__main__":
    count = 0
    width = len(board)
    length = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                count += 1 if check_vertical(board, i, j, "Up") else 0
                count += 1 if check_vertical(board, i, j, "Down") else 0
                
                count += 1 if check_horizontal(board, i, j, "Right") else 0
                count += 1 if check_horizontal(board, i, j, "Left") else 0
                
                count += 1 if check_diagonal(board, i, j, "Up_Left") else 0
                count += 1 if check_diagonal(board, i, j, "Down_Left") else 0
                count += 1 if check_diagonal(board, i, j, "Up_Right") else 0
                count += 1 if check_diagonal(board, i, j, "Down_Right") else 0
    print(count)