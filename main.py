# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:47:23 2016

@author: Rahul Patni
"""
import os
import sys

# Tic Tac Toe

CELL_SIZE = 7

gStatus = []
gBoard = []

def clearBoards():
    del gBoard[:]
    del gStatus[:]
    return

def initializeBoards(dim):
    [gBoard.append([' '] * dim) for num in range(dim)]
    [gStatus.append([-1] * 3) for num in range(3)]
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

def drawX(row, col):
    xOffset = (col - 1) * (CELL_SIZE + 1) + 1
    yOffset = (row - 1) * (CELL_SIZE + 1) + 1
    if gStatus[row - 1][col - 1] != -1:
        return False
    for i in range(CELL_SIZE):
        for j in range(CELL_SIZE):
            if (i == 0 or i == CELL_SIZE - 1) and (j == 0 or j == CELL_SIZE - 1):
                gBoard[i + yOffset][j + xOffset] = "+"
            elif (i == j):
                gBoard[i + yOffset][j + xOffset] = "+"
            elif i == CELL_SIZE - j - 1:
                gBoard[i + yOffset][j + xOffset] = "+"
    gStatus[row - 1][col - 1] = 0
    return True

def drawO(row, col):
    xOffset = (col - 1) * (CELL_SIZE + 1) + 1
    yOffset = (row - 1) * (CELL_SIZE + 1) + 1
    if gStatus[row - 1][col - 1] != -1:
        return False
    for i in range(CELL_SIZE):
        for j in range(CELL_SIZE):
            if i == 0 or i == CELL_SIZE - 1 or j == 0 or j == CELL_SIZE - 1:
                gBoard[i + yOffset][j + xOffset] = "o"
    gStatus[row - 1][col - 1] = 0
    return True
    
def playGame():
    os.system('cls')
    isPlayerOneChance = True
    initializeBoards(3 * (CELL_SIZE + 1) + 1)
    printBoard()
    while(True):
        if (isPlayerOneChance == True):
            print "Player 1's Turn."
            location = raw_input("Enter location To Place X (row, col): ")
            if location == "end":
                break
            try:
                row = int(location.split(",")[0])
                col = int(location.split(",")[1])
                if row > 3 or row < 1 or col < 1 or col > 3:
                    raise Exception() 
            except:
                print "\nError! Enter integers between 1 and 3\n"
                continue
            if drawX(row, col) == False:
                print "\nTry another spot.\n"
                continue
            isPlayerOneChance = False
        else:
            print "Player 2's Turn."
            location = raw_input("Enter location To Place O (row, col): 1, 1: ")
            if location == "end":
                break
            try:
                row = int(location.split(",")[0])
                col = int(location.split(",")[1])
                if row > 3 or row < 1 or col < 1 or col > 3:
                    raise Exception() 
            except:
                print "\nError! Enter integers between 1 and 3\n"
                continue
            if drawO(row, col) == False:
                print "\nTry another spot.\n"
                continue
            isPlayerOneChance = True
        printBoard()
    print "\nGame Over!"
    playAgain = raw_input("Play again y/n?: ")
    if (playAgain == "y"):
        clearBoards()
        playGame()
    
    
def main():
    playGame()
    
if __name__ == "__main__":
    main()