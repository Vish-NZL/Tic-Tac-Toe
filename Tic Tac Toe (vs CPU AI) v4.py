# This version of the game includes several updates:
# adds an "Easy" and "Hard" CPU opponent that you can select at the start of the game
# adds win and toe stats for player and cpu
# adds a coinflip at start of the game to see who goes first
# adds a replay feature after game ends
# remembers the difficulty you selected at the start of the game if you choose to play again,
# fixing the issue of the game asking to choose a difficulty every replay

import random

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
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_conditions)

# Function to check for a tie
def check_tie(board):
    return all(space != " " for space in board)

# Easy mode: Computer makes a random move
def computer_easy_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

# Hard mode: Computer checks for win or block
def computer_hard_move(board):
    # Check if the computer can win in the next move
    for move in range(9):
        if board[move] == " ":
            board[move] = "O"
            if check_win(board, "O"):
                return
            else:
                board[move] = " "  # Undo move

    # Check if the player could win on the next move, and block them
    for move in range(9):
        if board[move] == " ":
            board[move] = "X"
            if check_win(board, "X"):
                board[move] = "O"  # Block the player's win
                return
            else:
                board[move] = " "  # Undo move

    # Otherwise, pick a random move
    computer_easy_move(board)

# Function to ask if player wants to play again
def play_again():
    choice = input("Do you want to play again? (Yes/No): ").lower()
    return choice == "yes"

# Main game function
def play_game():
    player_wins = 0
    cpu_wins = 0
    ties = 0
    difficulty = None

    while True:
        board = [" " for _ in range(9)]  # Initialize empty board

        # Ask the user to choose difficulty only for the first game
        if difficulty is None:
            difficulty = input("Choose difficulty (Easy/Hard): ").lower()

            while difficulty not in ['easy', 'hard']:
                difficulty = input("Invalid choice. Please choose 'Easy' or 'Hard': ").lower()

        # Randomly decide who goes first
        player = random.choice(["X", "O"])
        if player == "X":
            print("You go first!")
        else:
            print("Computer goes first!")

        # Start the game loop
        while True:
            print_board(board)

            if player == "X":
                # Player's turn
                move = int(input("Choose your move (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = player
                else:
                    print("Invalid move. Try again.")
                    continue
            else:
                # Computer's turn
                print("Computer's turn...")
                if difficulty == "easy":
                    computer_easy_move(board)
                else:
                    computer_hard_move(board)

            # Check if the current player has won
            if check_win(board, player):
                print_board(board)
                if player == "X":
                    print("Congratulations! You win!")
                    player_wins += 1
                else:
                    print("Computer wins! Better luck next time.")
                    cpu_wins += 1
                break

            # Check for a tie
            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                ties += 1
                break

            # Switch players
            player = "O" if player == "X" else "X"

        # Display stats
        print(f"\n--- Game Stats ---")
        print(f"Player Wins: {player_wins}")
        print(f"CPU Wins: {cpu_wins}")
        print(f"Ties: {ties}\n")

        # Ask if the player wants to play again
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
