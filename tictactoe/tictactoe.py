"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):#OK
    numX = 0
    numO = 0
    numEmpty = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numX += 1
            elif board[i][j] == O:
                numO += 1
            else:
                numEmpty += 1
                
    if numEmpty == 9 or numX == numO :
        
        return X
    elif numX > numO:
        
        return O
    else:
        return None
        
    """
    Returns player who has the next turn on a board.
    """


def actions(board): # OK
    possibleActions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i,j))
    
    return possibleActions

    """
    Returns set of all possible actions (i, j) available on the board.
    """
    


def result(board, action): # OK
    
        
    turn = player(board)
    copyBoard = copy.deepcopy(board)
    copyBoard[action[0]][action[1]] = turn
    
    return copyBoard
    """
    Returns the board that results from making move (i, j) on the board.
    """
    


def winner(board): 
    
    
    
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == X:
                return X
            elif board[0][i] == O:
                return O
    if  board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == X:
                return X
            elif board[0][0] == O:
                return O
    if  board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == X:
                return X
            elif board[0][2] == O:
                return O
        
    
    
            
    """
    Returns the winner of the game, if there is one.
    """
    


def terminal(board):
    
    if winner(board) != None:
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True
    """
    Returns True if game is over, False otherwise.
    """
    


def utility(board):
    
    winnerPlayer = winner(board)
    if terminal(board):
        if winnerPlayer == X:
            return 1
        elif winnerPlayer == O:
            return -1
        else:
            return 0
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    


def minimax(board):
    
    if terminal(board):
        return None
    
    if player(board) == X:
        currScore = -1000
        bestMove = None
        for action in actions(board):
            bestScore = minValue(result(board,action))
            
            if bestScore > currScore:
                currScore = bestScore
                bestMove = action
        
        
    elif player(board) == O:
        currScore = 1000
        bestMove = None
        for action in actions(board):
            bestScore = maxValue(result(board,action))
            if bestScore < currScore:
                currScore = bestScore
                bestMove = action
        
    return bestMove       


def maxValue(board):
    if terminal(board):
        return utility(board)
    
    highestScore = -1000
    for action in actions(board):
        highestScore = max(highestScore,minValue(result(board,action)))
    return highestScore

def minValue(board):
    if terminal(board):
        return utility(board)
    
    lowestScore = 1000
    for action in actions(board):
        lowestScore = min(lowestScore,maxValue(result(board,action)))
    
    return lowestScore
    
        
    
    
    
        
        
    
