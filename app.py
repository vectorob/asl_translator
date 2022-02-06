## imports. 
import os, shutil, pickle
from flask import Flask, redirect, render_template, request, url_for, session
from flask_session import Session
from werkzeug.utils import secure_filename
from skimage.io import imread
from skimage.transform import resize 
from skimage import filters

## For testing, use sys package to print to console 
## import sys

## Load translation model
model = pickle.load(open("finalized_model.sav", 'rb'))

## *********** ##
## Copy the path to the upload folder on your local machine and paste it here: ##
UPLOAD_FOLDER = '/workspaces/43413436/Final2/static/uploads'
## *********** ##

## Declare array of allowable file extensions
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}

## start session
app = Flask(__name__)
app.secret_key = b'aslifjsdgho4it03'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Session(app)

## check upload has valid name and is a png or jpg
def allowed_file(filename):
    if '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False
           

## home page
@app.route('/')
def index():
    ## every time app is reloaded, clear upload folder

    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)

    ## return home page. No alerts, no file selected. 
    return render_template("index.html", result = '', file_selected = '', alert = 'hidden')

## upload files to folder
@app.route('/upload', methods=["GET", "POST"])
def upload():

    ## if user has uploaded a file, retrieve it from the request
    if request.method == 'POST':
        if request.files:
            file = request.files['file']

            ## check if filename is secure
            filename = secure_filename(file.filename)

            ## if filename is secure, save the file in uploads folder
            if file and allowed_file(filename):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                return render_template("index.html", filename = filename, alert = 'hidden')
            else:
                return render_template("index.html", message = 'Please submit a JPEG or PNG file', alert = 'visible')
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

## retrieve user upload and convert it to English
@app.route('/translate', methods = ['GET', 'POST'])
def translate():
    
    ## try to load the most recently uploaded file, getting it's path from the request's hidden input 
    if request.method == 'POST':
        path = 'static/uploads/' + request.form.get('filename')
        try:

            ## using skimage imread, store upload in an object for analysis
            file = imread(path)
        except:

        ## if the file cannot be read using imread, send alert to user
            return render_template('index.html', message = 'You must confirm your upload before translating', alert = 'visible')
        
        ## make prediction
        if request.form['submit_button'] == 'Translate':
            newimg = filters.sobel(resize(file, (100, 100, 1), anti_aliasing=True)).flatten()
            pred = model.predict([newimg])
        
        ## display prediction
        return render_template('index.html', result = pred[0], alert = 'hidden')
    else:
        return render_template('index.html')

## display uploaded file in left box
@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename))