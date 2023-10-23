from flask import Flask

app = Flask(__name__)


# Create our first route
@app.route("/")
def hello_world():
    name = 'Brian'
    return "<p>Hello, World!</p>"

# Create a second route
@app.route('/new')
def new():
    name = 'Brian Stanton'
    return f"<h1>Hello {name}, this is a new route! <\h1>"