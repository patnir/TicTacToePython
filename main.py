# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:47:23 2016

@author: Rahul Patni
"""
import os
import sys

# Tic Tac Toe

CELL_SIZE = 6

gStatus = []
gBoard = []

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
    
def clearBoards():
    del gBoard[:]
    del gStatus[:]
    return
    
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
            if i == j or i == CELL_SIZE - j - 1:
                gBoard[i + yOffset][j + xOffset] = "+"
    gStatus[row - 1][col - 1] = 1
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
    moves = 0
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
        moves += 1
        printBoard()
        if (checkWinner() == True):
            if isPlayerOneChance == False:
                print "\n\nPlayer 1 is the winner!\n"
            else:
                print "\n\nPlayer 2 is the winner!\n"
            break
        if (moves == 9):
            break
    print "\nGame Over!\n"
    playAgain = raw_input("Play again y/n?: ")
    if (playAgain == "y"):
        clearBoards()
        playGame()

def checkWinner():
    diag1 = gStatus[0][0]
    diag2 = gStatus[len(gStatus) - 1][0]
    diag1Difference = 0
    diag2Difference = 0
    for i in range(len(gStatus)):
        row = gStatus[i][0]
        col = gStatus[0][i]
        rowDifference = 0
        colDifference = 0
        for j in range(0, len(gStatus)):
            if row != gStatus[i][j]:
                rowDifference += 1
            if col != gStatus[j][i]:
                colDifference += 1
            if i == j and diag1 != gStatus[i][j]:
                    diag1Difference += 1
            if i == 2 - j and diag2 != gStatus[i][j]:
                    diag2Difference += 1
        if rowDifference == 0 and row != -1:
            print "row"
            return True
        if colDifference == 0 and col != -1:
            print "col"
            return True
    if diag1Difference == 0 and diag1 != -1:
            print "diag1"
            return True
    if diag2Difference == 0 and diag2 != -1:
        print "diag2"
        return True
    return False
    
def main():
    playGame()
    
if __name__ == "__main__":
    main()