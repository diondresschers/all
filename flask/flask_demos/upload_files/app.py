import imghdr # needed for the by us created function `validate_image`
import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from flask import send_from_directory # Necessary if NOT is send from the 'static' folder.

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.svg', '.jpeg', '.pdf', '.md']
app.config['UPLOAD_PATH'] = 'static/uploads' # Make sure that you upload this file first!

# Here no decorator as this is NO route
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))

# This is necessary if the file is NOT stored inside the 'static' folder.
@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/uploads/show_all')
def uploads_show_all():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('uploads_show_all.html', files=files)