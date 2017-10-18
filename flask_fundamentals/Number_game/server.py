from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def index():
  return render_template('index.html')


def num():
    print "score"
    for i in range(100):
        print "You actually did something"
        game = random.randint(0, 100)
        print num

app.run(debug=True)
