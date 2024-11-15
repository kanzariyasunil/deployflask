from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "this is my flask app"

@app.route('/yourname')
def yourname():
    return "Enter your name url"

@app.route('/yourname/<id>')
def enter(id):
    return render_template('index.html',id = id)
