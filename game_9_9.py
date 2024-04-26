from game_X_O import  is_board_full
def create_small_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def create_big_board():
    return [create_small_board() for _ in range(9)]

def make_move_9_9(big_board, board_index, move, player):
    small_board = big_board[board_index]
    row, col = move
    if small_board[row][col] == " ":
        small_board[row][col] = player
        return True
    return False

def fill_small_board(small_board, symbol):
    for i in range(3):
        for j in range(3):
            small_board[i][j] = symbol
def fill_small_board_if_dominated(small_board):
    count_X = sum(cell == 'X' for row in small_board for cell in row)
    count_O = sum(cell == 'O' for row in small_board for cell in row)
    if count_X > count_O:
        fill_small_board(small_board, 'X')
    elif count_O > count_X:
        fill_small_board(small_board, 'O')
def check_big_winner(big_board):
    for row in range(3):
        if big_board[row * 3][0][0] == big_board[row * 3 + 1][0][0] == big_board[row * 3 + 2][0][0] != " ":
            return big_board[row * 3][0][0]
    for col in range(3):
        if big_board[col][0][0] == big_board[col + 3][0][0] == big_board[col + 6][0][0] != " ":
            return big_board[col][0][0]
    if big_board[0][0][0] == big_board[4][0][0] == big_board[8][0][0] != " ":
        return big_board[0][0][0]
    if big_board[2][0][0] == big_board[4][0][0] == big_board[6][0][0] != " ":
        return big_board[2][0][0]
    if is_big_board_full(big_board):
        return 'Ничья'
    return None

def is_big_board_full(big_board):
    return all(is_board_full(small_board) for small_board in big_board)