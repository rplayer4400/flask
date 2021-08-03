from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Romeos'
    return render_template('index.html',my_name=name)

@app.route('/me')
def me():
    food = ['Patsa', 'Tacos', 'BBQ', 'Caribean food']
    return render_template('index.html', food=food)