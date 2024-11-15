from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1><b>This is virtual enviroment</b></h1>"

if __name__ == "__main__":
    app.run(debug=True)