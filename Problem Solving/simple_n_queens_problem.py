# Python Program for N-Queen Problem

# Function to print the solution
def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Function to check if placing a queen is safe
def is_safe(board, row, col, N):

    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Function to solve N-Queen using Backtracking
def solve_nqueen(board, col, N):

    # All queens are placed
    if col >= N:
        return True

    # Try placing queen in every row
    for row in range(N):

        if is_safe(board, row, col, N):

            board[row][col] = 1

            if solve_nqueen(board, col + 1, N):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Main Program
N = 4

board = [[0 for i in range(N)] for j in range(N)]

if solve_nqueen(board, 0, N):
    print("Solution:")
    print_solution(board, N)
else:
    print("No solution exists.")