from flask import Flask, render_template, redirect, url_for, request
import sys
import os
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/pi/Desktop/Flask_Git/FriggFlask/uploaded_files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template('index.html')
	#variable = request.form
	#return(sys.version) SHOWS PYTHON VERSION
	
	
	
@app.route('/getData', methods = ['POST','GET'])#if 'methods' is not declared, the default is GET
def get_event():
	print("Initialize printer")

	#FORM DATA REQUEST
	result = request.form
	print(result)
	print(result["texto"])
	
	#FILE UPLOADING
	f = request.files['file']
	filename = secure_filename(f.filename)
	f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
	#return render_template('index.html') !DONT RENDER THE TEMPLATE, CALL THE FUNCTION WHICH DOES
	return redirect(url_for('index')) #import 'redirect' and 'url_for' (top)

@app.route('/stopPrinting', methods = ['POST','GET'])
def stop_event():
	print("Stop printer")
	return redirect(url_for('index'))



if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
