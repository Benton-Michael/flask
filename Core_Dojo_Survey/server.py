from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "super secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    
