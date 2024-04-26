from flask import Flask, render_template 
import sqlite3 
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    conn = sqlite3.connect('bd_tic-tac-toe.db') 
    c = conn.cursor() 
    c.execute('SELECT * FROM users') 
    data = c.fetchall() 

    conn.close() 
 
    return render_template('home.html', data=data) 
 
if name == '__main__': 
    app.run(debug=True)
