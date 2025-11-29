# Check if a queen can be placed safely 
def is_safe(board, row, col):
    # Check the same column and diagonals 
    for i in range(row):
        if (board[i] == col or
            board[i] - i == col - row or
            board[i] + i == col + row):
            return False
    return True

# Place queens using backtracking 
def solve(board, row, n):
    if row == n:  # All queens placed
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col           # Place queen 
            solve(board, row + 1, n)   # Recur for next row 
            board[row] = -1            # Backtrack 

# Print the board 
def print_board(board, n):
    for i in range(n):
        row = ['.'] * n 
        row[board[i]] = 'Q'
        print(' '.join(row))
    print()

# Driver code (changed input size)
n = 8   
board = [-1] * n
print("Solutions for the 8 Queens Problem:")
solve(board, 0, n)
