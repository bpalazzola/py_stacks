from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result')
def result():
    return render_template('results.html')
app.run(debug=True)
