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
    
def playGame():
    isPlayerOneChance = True
    initializeBoard(3 * (CELL_SIZE + 1) + 1)
    printBoard()
    while(True):
        if (isPlayerOneChance == True):
            print "Player 1's Turn."
            location = raw_input("Enter location To Place X e.g: 1, 1: ")
            if location == "end":
                break
            try:
                x = int(location.split(",")[0])
                y = int(location.split(",")[1])
                if x > 3 or x < 1 or y < 1 or y > 3:
                    raise Exception() 
            except:
                print "\nError! Enter integers between 1 and 3\n"
                continue
            drawX(x, y)
            isPlayerOneChance = False
        else:
            print "Player 2's Turn."
            location = raw_input("Enter location To Place O e.g: 1, 1: ")
            if location == "end":
                break
            try:
                x = int(location.split(",")[0])
                y = int(location.split(",")[1])
                if x > 3 or x < 1 or y < 1 or y > 3:
                    raise Exception() 
            except:
                print "\nError! Enter integers between 1 and 3\n"
                continue
            drawO(x, y)
            isPlayerOneChance = True
        printBoard()
    print "\nGame Over!"
    playAgain = raw_input("Play again y/n?: ")
    if (playAgain == "y"):
        playGame()
    
def main():
    playGame()
    
if __name__ == "__main__":
    main()