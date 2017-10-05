from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    my_projects = ['Ninja Gold', 'Great Number Game',
                   'Disappearing Ninjas', 'Dojo Survey']
    return render_template('projects.html', projects=my_projects)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)