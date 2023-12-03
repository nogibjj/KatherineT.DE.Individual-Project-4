import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('home.html', title='Home')

@app.route('/index')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)