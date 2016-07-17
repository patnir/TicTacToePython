# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:47:23 2016

@author: Rahul Patni
"""
import sys

# Tic Tac Toe

CELL_SIZE = 3

def drawBoard():
    length = 3 * (CELL_SIZE + 1) + 1
    for i in range(length):
        if i % (CELL_SIZE + 1) == 0:
            for j in range(length):
                if j % (CELL_SIZE + 1) == 0:
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write("-")
        else:
            for j in range(length):
                if j % (CELL_SIZE + 1) == 0:
                    sys.stdout.write("|")
                else:
                    sys.stdout.write(" ")
        sys.stdout.write("\n")
    return 
    
def drawX(x, y):
    for i in range(CELL_SIZE):
        for j in range(CELL_SIZE):
            if (i == 0 or i == CELL_SIZE - 1) and (j == 0 or j == CELL_SIZE - 1):
                sys.stdout.write("+")
            elif (i == j):
                sys.stdout.write("+")
            elif i == CELL_SIZE - j - 1:
                sys.stdout.write("+")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")
    return

def drawO(x, y):
    for i in range(CELL_SIZE):
        for j in range(CELL_SIZE):
            if i == 0 or i == CELL_SIZE - 1 or j == 0 or j == CELL_SIZE - 1:
                sys.stdout.write("o")
            else: 
                sys.stdout.write(" ")
        sys.stdout.write("\n")
    return
    
def main():
    drawBoard()
    #drawO(0,0)
    
if __name__ == "__main__":
    main()