def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print("\n" + "-" * (len(board) * 2 - 1) + "\n")

def is_safe(board, row, col, n):
    # Check left side, upper diagonal, and lower diagonal
    for i in range(col):
        if board[row][i] == 1: return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1: return False
    return True

def solve_n_queens_util(board, col, n, solutions_count):
    if col >= n:
        solutions_count[0] += 1
        print(f"Solution #{solutions_count[0]}:")
        print_board(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions_count)
            board[i][col] = 0 # Backtrack

def solve_n_queens(n):
    if n < 1: return
    board = [[0] * n for _ in range(n)]
    solutions_count = [0]
    solve_n_queens_util(board, 0, n, solutions_count)
    print(f"Total solutions found: {solutions_count[0]}")

if __name__ == "__main__":
    solve_n_queens(4)
