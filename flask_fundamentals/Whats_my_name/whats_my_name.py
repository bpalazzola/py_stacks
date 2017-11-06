from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=['POST'])
def process_form():
    name = request.form['name'];
    print request.form
    return render_template("/success.html", name=name)

app.run(debug=True)
