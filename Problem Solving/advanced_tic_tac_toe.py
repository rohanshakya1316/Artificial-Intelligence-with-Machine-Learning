import math

board = [' ' for _ in range(9)]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def is_winner(bo, le):
    return (bo[0] == le and bo[1] == le and bo[2] == le) or \
           (bo[3] == le and bo[4] == le and bo[5] == le) or \
           (bo[6] == le and bo[7] == le and bo[8] == le) or \
           (bo[0] == le and bo[3] == le and bo[6] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[0] == le and bo[4] == le and bo[8] == le) or \
           (bo[2] == le and bo[4] == le and bo[6] == le)

def evaluate(bo):
    if is_winner(bo, 'X'):
        return 1
    elif is_winner(bo, 'O'):
        return -1
    else:
        return 0

def is_board_full(bo):
    return ' ' not in bo

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # If Maximizer (X) has won the game return score
    if score == 1:
        return score

    # If Minimizer (O) has won the game return score
    if score == -1:
        return score

    # If there are no more moves and no winner then it is a tie
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# --- ADD THIS TO THE END OF YOUR FILE TO RUN THE GAME ---

def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'O', AI is 'X'.")
    print_board(board)
    
    while not is_board_full(board) and evaluate(board) == 0:
        # Player turn (O)
        try:
            player_move = int(input("Enter your move (0-8): "))
            if board[player_move] != ' ':
                print("Spot taken! Try again.")
                continue
            board[player_move] = 'O'
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 0 and 8.")
            continue
            
        print_board(board)
        
        # Check if player won or tied
        if evaluate(board) == -1 or is_board_full(board):
            break
            
        # AI turn (X)
        print("\nAI is thinking...")
        ai_move = find_best_move(board)
        if ai_move != -1:
            board[ai_move] = 'X'
        
        print_board(board)

    # Game Over Checks
    if evaluate(board) == 1:
        print("AI wins! Better luck next time.")
    elif evaluate(board) == -1:
        print("You win! (Should be impossible against Minimax)")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
