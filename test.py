# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_pymongo import PyMongo
from pprint import pprint
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'saveory' 
app.config['MONGO_URI'] = 'mongodb://localhost:27017/saveory'

mongo = PyMongo(app)

csrf = CSRFProtect(app)

@app.route('/')
def home():
	return render_template('a.html')

@app.route('/add')
def add():
	user = mongo.db.users
	user.insert( {
		"first_name" : "t",
		"last_name" : "h" 
	})
	return "Res"

@app.route('/find')
def find():
	user = mongo.db.users
	res = user.find_one({'first_name' : 't'})
	pprint(res)
	temp = res['first_name']
	print(temp)
	res.update( {'first_name' : "w"} )
	pprint(res) 
	res1 = user.find_one({'first_name' : 'j' })
	pprint(res1)
	return "yes"

if __name__ == '__main__':
    app.secret_key = '$aveory'
    app.run(host='0.0.0.0',debug=True)
