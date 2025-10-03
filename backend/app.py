# app.py
from flask import Flask, render_template, jsonify, request
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'counter.db'

# Initialiser la base de données
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS counter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER NOT NULL
        )
    ''')
    
    # Insérer une valeur initiale si la table est vide
    cursor.execute("SELECT COUNT(*) FROM counter")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO counter (value) VALUES (0)")
    
    conn.commit()
    conn.close()

# Route principale pour afficher la page
@app.route('/')
def index():
    return render_template('index.html')

# Route pour obtenir la valeur actuelle du compteur
@app.route('/api/get-counter', methods=['GET'])
def get_counter():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    value = cursor.fetchone()[0]
    conn.close()
    return jsonify({'value': value})

# Route pour incrémenter le compteur
@app.route('/api/increment', methods=['POST'])
def increment_counter():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = value + 1 WHERE id = 1")
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    new_value = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return jsonify({'value': new_value})

# Route pour réinitialiser le compteur
@app.route('/api/reset', methods=['POST'])
def reset_counter():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = 0 WHERE id = 1")
    conn.commit()
    conn.close()
    return jsonify({'value': 0})

# Route pour incrémenter de 10
@app.route('/api/increment-ten', methods=['POST'])
def increment_ten():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = value + 10 WHERE id = 1")
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    new_value = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return jsonify({'value': new_value})

# Route pour décrémenter de 1
@app.route('/api/decrement', methods=['POST'])
def decrement_counter():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = value - 1 WHERE id = 1")
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    new_value = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return jsonify({'value': new_value})

# Route pour décrémenter de 10
@app.route('/api/decrement-ten', methods=['POST'])
def decrement_ten():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = value - 10 WHERE id = 1")
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    new_value = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return jsonify({'value': new_value})

# Ce bloc doit TOUJOURS être à la fin
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
