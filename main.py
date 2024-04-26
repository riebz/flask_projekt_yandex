from flask import Flask, render_template, request, redirect, url_for, session
from game_X_O import create_board, check_winner, is_board_full, make_move
from game_9_9 import create_big_board, make_move_9_9, check_big_winner, is_big_board_full

app = Flask(__name__)
app.secret_key = 'very_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        size = int(request.form.get('board_size', 3))
        session.clear()
        session['size'] = size
        if size == 9:
            session['big_board'] = create_big_board()
        else:
            session['board'] = create_board()
        session['current_player'] = 'X'
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    size = session.get('size', 3)
    current_player = session.get('current_player', 'X')
    winner = session.get('winner', None)

    if request.method == 'POST':
        if 'new_game' in request.form:
            return redirect(url_for('/'))

        move = request.form.get('move')
        if move:
            moves = move.split('_')
            if size == 9 and len(moves) == 3:
                board_index, row, col = map(int, moves)
                if make_move_9_9(session['big_board'], board_index, (row, col), current_player):
                    winner = check_big_winner(session['big_board'])
                    session['winner'] = winner
            else:
                row, col = map(int, moves)
                if make_move(session['board'], row, col, current_player):
                    winner = check_winner(session['board'])
                    session['winner'] = winner

            if not winner:
                if (size == 9 and is_big_board_full(session['big_board'])) or (size != 9 and is_board_full(session['board'])):
                    session['winner'] = 'Ничья'
                else:
                    session['current_player'] = 'O' if current_player == 'X' else 'X'

    if size == 9:
        return render_template('game_9_9.html', big_board=session['big_board'], size=size, winner=winner)
    else:
        return render_template('game.html', board=session['board'], size=size, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)