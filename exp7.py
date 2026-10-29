# EXP-7 8 QUEENS PROBLEMS

# function to print a cheasboard
def print_board(board):
    for row in board:
        print(" ".join(row))

# function to check if a queen can be placed safely
def is_safe(board, row, col):
    # Check for queens in the same row to the left
    for i in range(col):
        if board[row][i]=="Q":
            return False

    # Check for queens in the same column above
    for i in range(row):
        if board[i][col]=="Q":
            return False

    # Check upper_left diagonal
    i, j = row - 1, col - 1
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1

    # Check upper_right diagonal
    i, j = row - 1, col + 1
    while i>=0 and j< 8:
        if board[i][j] =='Q':
            return False
        i-=1
        j+=1
    return True

# backtracking function
def solved(board,row):
    if row==8:
        return True

    for  col in range(8):
        if is_safe(board,row,col):
            board[row][col]='Q'

            if solved(board,row+1):
                return True
            board[row][col]='.' # Backtrack
    return False

# main program
board =[['.' for _ in range(8)] for _ in range(8)]

if solved(board,0):
    print("\n solution for the 8-queens problem:\n")
    print_board(board)
else:
    print("\n no solution exists")

    '''--------OUTPUT--------
    [ ]


 solution for the 8-queens problem:

Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
    
    
    '''