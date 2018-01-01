from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
	return "post"
    return  "register"

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return "signig"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
