# Tic-Tac-Toe Game in Python

# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Function to check for a win
def check_win(board, mark):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]  # Diagonals
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_conditions)


# Function to check for a tie
def check_tie(board):
    return all(space != " " for space in board)


# Main game function
def play_game():
    board = [" " for _ in range(9)]  # Initialize empty board
    current_player = "X"  # X goes first

    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
