from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    python_string = "Hello World from Jinja2"
    return render_template('index.html', jinja_string=python_string)