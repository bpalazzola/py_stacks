from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendship')
# an example of running a query
print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_friend', methods=['POST'])
def create_friend():
    name = request.form['name']
    age = request.form['age']
    created_at = datetime.datetime.now()
    mysql.query_db("INSERT INTO friends(name, age) VALUES('{}', '{}')".format(name, age))
    print name, age
    return redirect('/')

app.run(debug=True)
