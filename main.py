from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

from game_X_O import create_board, check_winner, is_board_full, reset_game
from game_9_9 import create_big_board, make_move, check_big_winner, is_big_board_full
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        size = int(request.form['board_size'])
        session['size'] = size  # Сохраняем выбранный размер в сессии
        if size == 9:
            session['big_board'] = create_big_board()  # Для игры 9x9
            session['current_player'] = 'X'
        else:
            session['board'] = create_board(size)  # Для игры 3x3
            session['current_player'] = 'X'
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    size = session.get('size')  # Получаем размер поля из сессии
    current_player = session.get('current_player', 'X')
    winner = session.get('winner', None)
    if 'new_game' in request.form:
        reset_game(session)  # Сброс игры
        return redirect(url_for('game'))
    # Если в сессии нет доски, создаем новую
    if size == 9:
        # Инициализируем большое поле 9x9, если оно еще не создано
        if 'big_board' not in session:
            session['big_board'] = create_big_board()
        big_board = session['big_board']
        # Остальная логика игры
        if request.method == 'POST':
            if 'new_game' in request.form:
                # Сброс игры
                session.clear()
                return redirect(url_for('index'))

            move = request.form.get('move')
            if move:
                row, col = map(int, move.split('_'))
                current_player = session.get('current_player', 'X')
                if make_move(big_board, (row, col), current_player):
                    # Проверяем, есть ли победитель на большом поле
                    winner = check_big_winner(big_board)
                    if winner:
                        session['winner'] = winner
                    elif is_big_board_full(big_board):
                        session['winner'] = 'Ничья'
                    else:
                        # Смена игрока
                        next_player = 'O' if current_player == 'X' else 'X'
                        session['current_player'] = next_player
                    session['big_board'] = big_board  # Сохраняем обновленное состояние доски

        # Рендерим шаблон для большого поля 9x9
        return render_template('game_9_9.html', big_board=big_board, size=size, winner=session.get('winner'))
    elif size == 3:
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