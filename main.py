from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def create_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]


def check_winner(board, player):
    size = len(board)
    for i in range(size):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(size)):
            return True
    if all(board[i][i] == player for i in range(size)) or all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    size = session.get('size')
    if size is None:
        size = 3
        session['size'] = size

    board = session['board']
    current_player = session['current_player']
    winner = None

    if request.method == 'POST':
        move = request.form.get('move')
        if move:
            row, col = map(int, move.split('_'))
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    winner = current_player
                elif is_board_full(board):
                    winner = 'Ничья'
                else:
                    session['current_player'] = 'O' if current_player == 'X' else 'X'
            session.modified = True

    return render_template('game.html', board=board, size=size, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)##