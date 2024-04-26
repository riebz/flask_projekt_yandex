
def create_board(size=3):
    return [[" " for _ in range(size)] for _ in range(size)]

def reset_game(session):
    session['board'] = create_board(session.get('size', 3))
    session['current_player'] = 'X'
    session['winner'] = None

def is_valid_move(board, row, col):
    return board[row][col] == " "

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_winner(board):
    size = len(board)
    for i in range(size):
        if all(cell == board[i][0] != " " for cell in board[i]):
            return board[i][0]
        if all(board[j][i] == board[0][i] != " " for j in range(size)):
            return board[0][i]
    if all(board[i][i] == board[0][0] != " " for i in range(size)):
        return board[0][0]
    if all(board[i][size-1-i] == board[0][size-1] != " " for i in range(size)):
        return board[0][size-1]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

