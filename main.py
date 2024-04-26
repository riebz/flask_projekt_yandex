import requests, os
from flask import Flask, render_template, request, redirect, url_for, session
from game_X_O import create_board, check_winner, is_board_full, make_move
from game_9_9 import create_big_board, make_move_9_9, check_big_winner, is_big_board_full

app = Flask(__name__)
app.secret_key = '3d5cfb7d140b469535655b3dca1ce307'


app = Flask(__name__)
app.secret_key = '3d5cfb7d140b469535655b3dca1ce307'

API_KEY = '3d5cfb7d140b469535655b3dca1ce307'

API_KEY = os.getenv('3d5cfb7d140b469535655b3dca1ce307')

@app.route('/weather', methods=['GET'])
def weather():
    city = 'Moscow'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return render_template('weather.html', weather_data=weather_data)
    else:
        error_message = response.json().get('message', 'Error getting weather data')
        return f"Error getting weather data: {error_message}", response.status_code

users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        if username and username not in users:
            users[username] = {'username': username}
            session['username'] = username
            return redirect(url_for('index'))  # Перенаправление на главную страницу после регистрации
        else:
            error = "Это имя пользователя уже занято или некорректно."
            return render_template('register.html', error=error)
    return render_template('register.html')

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
            return redirect(url_for('index'))

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