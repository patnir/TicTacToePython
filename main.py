# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:47:23 2016

@author: Rahul Patni
"""
import sys

# Tic Tac Toe

CELL_SIZE = 5

gBoard = []

def initializeBoard(dim):
    [gBoard.append([' '] * dim) for num in range(dim)]
    length = len(gBoard)
    for i in range(length):
        if i % (CELL_SIZE + 1) == 0:
            for j in range(length):
                if j % (CELL_SIZE + 1) != 0:
                    gBoard[i][j] = "-"
        else:
            for j in range(length):
                if j % (CELL_SIZE + 1) == 0:
                    gBoard[i][j] = "|"
    return gBoard 
    
def printBoard():
    for i in range(len(gBoard)):
        for j in range(len(gBoard)):
            sys.stdout.write(gBoard[i][j]),
        sys.stdout.write("\n")

def drawX(x, y):
    xOffset = (x - 1) * (CELL_SIZE + 1) + 1
    yOffset = (y - 1) * (CELL_SIZE + 1) + 1
    for i in range(CELL_SIZE):
        for j in range(CELL_SIZE):
            if (i == 0 or i == CELL_SIZE - 1) and (j == 0 or j == CELL_SIZE - 1):
                gBoard[i + yOffset][j + xOffset] = "+"
            elif (i == j):
                gBoard[i + yOffset][j + xOffset] = "+"
            elif i == CELL_SIZE - j - 1:
                gBoard[i + yOffset][j + xOffset] = "+"
    return

def drawO(x, y):
    xOffset = (x - 1) * (CELL_SIZE + 1) + 1
    yOffset = (y - 1) * (CELL_SIZE + 1) + 1
    for i in range(CELL_SIZE):
        for j in range(CELL_SIZE):
            if i == 0 or i == CELL_SIZE - 1 or j == 0 or j == CELL_SIZE - 1:
                gBoard[i + yOffset][j + xOffset] = "o"
    return   
    
def main():
    initializeBoard(3 * (CELL_SIZE + 1) + 1)
    drawX(3, 3)
    drawO(3, 2)
    printBoard()
    
if __name__ == "__main__":
    main()