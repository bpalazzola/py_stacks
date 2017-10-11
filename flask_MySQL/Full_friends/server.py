from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'session key'
mysql_connection = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
    results = []
    query = 'select name, age, created_at from friends'
    results = mysql_connection.query_db(query)
    return render_template('index.html', friends=results)


@app.route('/addvalue', methods=['POST'])
def create():
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    if 'name' in session:
        parameters = {
            'parameter_name': session['name'],
            'parameter_age': session['age'],
        }
        query = 'insert into friends (name, age, created_at, updated_at) values (:parameter_name,:parameter_age, NOW(), NOW())'
        mysql_connection.query_db(query, parameters)
        session.clear()
    return redirect('/')


app.run(debug=True)
