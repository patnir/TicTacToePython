# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:47:23 2016

@author: Rahul Patni
"""
import os
import sys

# Tic Tac Toe

CELL_SIZE = 5

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
    
def drawSymbol(location, symbol):
    if (symbol == "X"):
        return drawX(location[0], location[1])
    return drawO(location[0], location[1])

def getInputs(currentPlayer, location):
    userInput = raw_input("Enter location To Place {} (row, col): ".format(currentPlayer))
    if userInput == "end":
        return False
    try:
        row = int(userInput.split(",")[0])
        col = int(userInput.split(",")[1])
    except:
        print "\nError! Enter integers between 1 and 3\n"
        return getInputs(currentPlayer, location)
    if row > 3 or row < 1 or col < 1 or col > 3:
        print "\nError! Enter integers between 1 and 3\n"
        return getInputs(currentPlayer, location)
    location[0] = row
    location[1] = col
    return True

def playGame():
    os.system('cls')
    currentPlayer = "X"
    initializeBoards(3 * (CELL_SIZE + 1) + 1)
    printBoard()
    moves = 0
    location = [0, 0]
    gameStatus = checkWinner()
    while(gameStatus == False and moves <= 9):
        if currentPlayer == "X":
            print "Player 1's Turn."
        else:
            print "Player 2's Turn."
        if getInputs(currentPlayer, location) == False:
            break
        if drawSymbol(location, currentPlayer) == False:
            print "\nTry another spot.\n"
        else:
            if currentPlayer == "O":
                currentPlayer = "X"
            else:
                currentPlayer = "O"
        printBoard()
        gameStatus = checkWinner()
        moves += 1
    print "\nGame Over!"
    if (gameStatus == True):
        if currentPlayer == "O":
            print "\n\nPlayer 1 is the winner!"
        else:
            print "\n\nPlayer 2 is the winner!"
    playAgain = raw_input("\nPlay again y/n?: ")
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
            return True
        if colDifference == 0 and col != -1:
            return True
    if diag1Difference == 0 and diag1 != -1:
        return True
    if diag2Difference == 0 and diag2 != -1:
        return True
    return False
    
def main():
    playGame()
    
if __name__ == "__main__":
    main()