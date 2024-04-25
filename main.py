from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

from game_X_O import create_board, check_winner, is_board_full, reset_game

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['board'] = create_board(3)
        session['current_player'] = 'X'
        session['size'] = 3
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'new_game' in request.form:
        reset_game(session)  # Сброс игры
        return redirect(url_for('game'))
    # Если в сессии нет доски, создаем новую
    if 'board' not in session:
        session['board'] = create_board(3)
        session['current_player'] = 'X'
        session['size'] = 3

    board = session['board']
    current_player = session['current_player']
    size = session['size']
    winner = None

    if request.method == 'POST':
        if 'new_game' in request.form:
            session.pop('board', None)
            session.pop('current_player', None)
            session.pop('size', None)
            return redirect(url_for('index'))

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
                session['board'] = board

    return render_template('game.html', board=board, size=size, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)