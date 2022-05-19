import os
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    files = os.listdir('uploads')
    for file in files:
        print(file)
    return render_template('index.html', files=files)


@app.route('/upload', methods=["POST"])
def upload():
    file = request.files['file']
    inputefilename = request.form['filename']
    extension = os.path.splitext(file.filename)[1]
    if file:
        if extension not in app.config['ALLOWED_EXTENSIONS']:
            return "File is not supported <a href='/'>Back to home</a>"
        else:
            file.save(f'uploads/{secure_filename(inputefilename.lower()) + extension}')

    else:
        return "Please add a file <a href='/'>Home</a>"
    return redirect('/')


@app.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory('uploads', filename)


app.run(host='0.0.0.0', port=81)
