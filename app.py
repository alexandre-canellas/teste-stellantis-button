from flask import Flask, render_template
import os
import signal
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/close-app')
def close_app():
    os.system('taskkill /f /im mspaint.exe')  # Alterar mspaint.exe pelo nome do app
    return "App closed"

if __name__ == '__main__':
    app.run(debug=True)