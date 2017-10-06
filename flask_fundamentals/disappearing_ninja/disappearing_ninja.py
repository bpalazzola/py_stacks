from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja')
def ninja():
    return render_template('ninja.html')


@app.route('/ninja/<color>')
def turtle_display(color):
    print color
    if color == 'blue':
        return render_template('blue.html')
    elif color == 'orange':
        return render_template('orange.html')
    elif color == 'purple':
        return render_template('purple.html')
    elif color == 'red':
        return render_template('red.html')
    else:
        return render_template('error.html')


app.run(debug=True)
