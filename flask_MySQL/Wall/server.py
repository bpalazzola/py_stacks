from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
#app.secret_key to enable 'POST' method
app.secret_key = '54b0c58c7ce9f2a8b551351102ee0938'
mysql = MySQLConnector(app, 'mydb')

#main registering or logging in page


@app.route('/')
def startpage():
    return render_template('login.html')

#route to registering validation address


@app.route('/register', methods=['POST'])
def register():
    #create variables holding the information 'inputed' from user trying to register
    first_name = str(request.form['first_name'])
    last_name = str(request.form['last_name'])
    email = request.form['email']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    #create variable to check whether all information from the input fields match set requirements, if any does not, it will hold a True to being NOT accurate/acceptable
    form_reproved = False
    #run checks on every parameter of the form
    if len(first_name) < 1:
        form_reproved = True
        flash("*First name cannot be empty!")
    if len(last_name) < 1:
        form_reproved = True
        flash("*Last name cannot be empty!")
    if len(password) < 1:
        flash("*Password cannot be empty!")
        form_reproved = True
    if len(password) >= 1 and len(pass_confirm) < 1:
        flash("*Please confirm password!")
        form_reproved = True
    if (len(password) >= 1 and len(pass_confirm) >= 1) and password != pass_confirm:
        flash("*Passwords do not match!")
        form_reproved = True
    if password.isnumeric() == True or password.isalpha() == True or password.islower() == True or password.isupper() == True:
        flash('*Password is requred to have at least 1 uppercase, 1 lowercase letter and 1 numeric value!')
        form_reproved = True
    if len(email) < 1:
        flash('*Email cannot be blank!')
        form_reproved = True
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("*Invalid Email Address!")
        form_reproved = True
        #if any of the information from user is unacceptable and the information have been rejected, send the user back to login/registration page with appropriate warnings
    if form_reproved == True:
        return redirect('/')
    else:
        #if all information is ok, hash the password before including in the database
        password = md5.new(password).hexdigest()
        #create the dictionary to hold information to be included in the SQL insert query
        parameters = {
            'parameter_first_name': first_name,
            'parameter_last_name': last_name,
            'parameter_email': email,
            'parameter_password': password,
        }
        #create variable with SQL insert query
        query = 'insert into users (first_name, last_name, email, password, created_at, updated_at) values (:parameter_first_name,:parameter_last_name,:parameter_email,:parameter_password, NOW(), NOW())'
        print query
        user_query = "SELECT * FROM users WHERE users.email = '{}' and users.password = '{}'".format(email,password)
        mysql.query_db(query, parameters)
        session['user'] = mysql.query_db(user_query, parameters)[0]
        print session['user']
        return redirect('/wall')

#route to log in validation address


@app.route('/login', methods=['POST'])
def login():
    #get submited username - e-mail address being the case
    login_username = request.form['username']
    #if field is empty, return flash message stating so - back to login page
    if len(login_username) < 1:
        flash("*You have to provide a user name!")
        return redirect('/')
    else:
        #set the results form which will include the results from the query
        results = []
        #hash the 'inputed' password to match the hashed in the database
        login_password = md5.new(request.form['password']).hexdigest()
        #create the dictionary to have values for the SQL query
        parameters = {
            'parameter_username': login_username,
            'parameter_password': login_password,
        }
        #create variable holding the SQL query - in this case to match the e-mails
        query = 'select first_name from users where email = :parameter_username'
        #save query to variable
        results = mysql.query_db(query, parameters)
        #in case e-mail do not match the one in the database, send user back to login page with a warning message
        if len(results) == 0:
            flash("*User name does not exist in our records!")
            return redirect('/')
        else:
            #in case e-mails match, try to match passwords
            results = []
            query = 'select id, first_name, last_name from users where email = :parameter_username and password = :parameter_password'
            mysql.query_db(query, parameters)
            results = mysql.query_db(query, parameters)
            #in case passwords don't match, send user back to query page with warning
            if len(results) == 0:
                flash("*Password does not match our records!")
                return redirect('/')
            #in case passwords match, create session variables with essential information send user to wall page
            else:
                session['user'] = results[0]
                address = '/wall'
                #create address variable so each user has its unique page address (firstname+lastname+id) -> eg wall/johnblack1
                return redirect(address)


@app.route('/wall')
def wall():
    query="SELECT * FROM messages"
    messages=mysql.query_db(query)
    return render_template('wall.html', messages=messages)



@app.route('/message/<id>', methods=['POST'])
def messages(id):
    message = request.form["new_message"]
    query="INSERT INTO messages (message, created_at, updated_at, users_id) values('{}',now(), now(),{})".format(message,id)
    mysql.query_db(query)
    return redirect('/wall')

@app.route('/comments', methods=['POST'])
def comments():
    return redirect('/wall')

#log out by clearing session and sending user back to login page


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
