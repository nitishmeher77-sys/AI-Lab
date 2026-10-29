# EXP-9 TIC-TAC-TOE PROBLEM


def print_board(board):
    for r in range(3):
        row_display = [board[r][c] if board[r][c] != "" else " " for c in range(3)]
        print(" " + " | ".join(row_display))
        if r < 2:
            print("---" * 3)

# function to check the winner
def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# main program
board = [["" for _ in range(3)] for _ in range(3)]
player = "X"

for turn in range(9):
    print("\nCurrent board:")
    print_board(board)
    print(f"Player {player}'s turn")

    # Get valid input
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == "":
                    board[row][col] = player
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid indices. Must be 0, 1, or 2.")
        except ValueError:
            print("Please enter valid integers.")

    winner = check_winner(board)
    if winner:
        print("\nFinal board:")
        print_board(board)
        print(f"\nPlayer {winner} wins!")
        break

    # Switch player
    player = "O" if player == "X" else "X"
else:
    print("\nFinal board:")
    print_board(board)
    print("\nIt's a draw!")

    '''----OUTPUT------

Current board:
   |   |  
---------
   |   |  
---------
   |   |  
Player X's turn


    '''