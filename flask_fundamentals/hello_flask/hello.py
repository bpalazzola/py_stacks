from flask import Flask  # Import Flask to allow us to create our app.
# Global variable __name__ tells Flask whether or not we are running the file
app = Flask(__name__)
# directly, or importing it as a module.


# The "@" symbol designates a "decorator" which attaches the following
@app.route('/')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return 'Hello World!'  # Return the string 'Hello World!' as a response.

@app.route('/hello_cats')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_cats():
  return 'Hello cats!'  # Return the string 'Hello World!' as a response.

@app.route('/hello_dogs')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_dogs():
  return 'Hello dogs!'  # Return the string 'Hello World!' as a response.

@app.route('/hello/<person>')
def hello_person(person):
    return "Hello " + person


app.run(debug=True)      # Run the app in debug mode.
