def create_board(size=3):
    return [[" " for _ in range(size)] for _ in range(size)]

def is_valid_move(board, row, col):
    return board[row][col] == " "

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_winner(board, player):
    size = len(board)
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True
    if all(board[i][i] == player for i in range(size)) or all(board[i][size-1-i] == player for i in range(size)):
        return True
    return False

def is_board_full(board):
    return all(board[row][col] != " " for row in range(len(board)) for col in range(len(board)))