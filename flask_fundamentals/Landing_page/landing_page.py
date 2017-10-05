from flask import Flask, render_template, render_static
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninjas')
def index():
    return render_template('ninjas.html')


@app.route('/dojo/new')
def dojo():
    return render_template('dojo.html')


app.run(debug=True)
