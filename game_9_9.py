def create_small_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_small_winner(small_board):
    for row in small_board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if small_board[0][col] == small_board[1][col] == small_board[2][col] != " ":
            return small_board[0][col]
    if small_board[0][0] == small_board[1][1] == small_board[2][2] != " ":
        return small_board[0][0]
    if small_board[0][2] == small_board[1][1] == small_board[2][0] != " ":
        return small_board[0][2]
    return None

def create_big_board():
    return [create_small_board() for _ in range(9)]

def get_small_board(big_board, move):
    board_index = (move[0] // 3) * 3 + (move[1] // 3)
    return big_board[board_index], board_index

def make_move(big_board, move, player):
    small_board, board_index = get_small_board(big_board, move)
    row, col = move[0] % 3, move[1] % 3
    if small_board[row][col] == " ":
        small_board[row][col] = player
        winner = check_small_winner(small_board)
        if winner:
            big_board[board_index] = [[winner]*3 for _ in range(3)]
        return True
    return False

def is_big_board_full(big_board):
    for small_board in big_board:
        for row in small_board:
            if " " in row:
                return False
    return True

def check_big_winner(big_board):
    for i in range(0, 9, 3):
        if big_board[i][0][0] == big_board[i+1][0][0] == big_board[i+2][0][0] != " ":
            return big_board[i][0][0]
        if big_board[0][i][0] == big_board[0][i+1][0] == big_board[0][i+2][0] != " ":
            return big_board[0][i][0]
    if big_board[0][0][0] == big_board[4][0][0] == big_board[8][0][0] != " ":
        return big_board[0][0][0]
    if big_board[2][0][0] == big_board[4][0][0] == big_board[6][0][0] != " ":
        return big_board[2][0][0]
    return None