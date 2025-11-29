def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 8)

def check_winner(board, player):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return any(all(board[r][c] == player for r, c in condition) for condition in win_conditions)

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Choose a number between 1 and 9.")
            continue

        if move < 0 or move > 8:
            print("Invalid input! Choose a number between 1 and 9.")
            continue

        row, col = divmod(move, 3)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That spot is already taken! Try again.")
            continue

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()