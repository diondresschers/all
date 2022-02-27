from flask import Flask
from flask import render_template
from flask import flash

app = Flask(__name__)
app.secret_key = 'dummy_geheim'

@app.route('/')
def index():
    flash('Bootstrap primary', 'primary')
    flash('Bootstrap secondary', 'secondary')
    flash('Bootstrap success', 'success')
    flash('Bootstrap danger', 'danger')
    flash('Bootstrap warning', 'warning')
    flash('Bootstrap info', 'info')
    flash('Bootstrap light', 'light')
    flash('Bootstrap dark', 'dark')

    return render_template('index.html')