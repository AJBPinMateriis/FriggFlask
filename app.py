from flask import Flask, render_template, redirect, url_for, request, jsonify
import sys, os, time
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/pi/Desktop/FriggFlask/uploaded_files'
#ALLOWED_EXTENSIONS = set(['txt']) #TRY LATER

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	className = "init_button"
	return render_template('index.html', color_class = className) #pass 'init_button' className to HTML tempalte using Jinja2
	#variable = request.form
	#return(sys.version) SHOWS PYTHON VERSION

	
@app.route('/getData', methods = ['POST'])#if 'methods' is not declared, the default is GET
def get_event():
	print("Initialize printer")

	#FORM DATA REQUEST
	result = request.form
	print(result)
	
	#FILE UPLOADING
	f = request.files['file']
	filename = secure_filename(f.filename)
	#print(filename)
	f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	#print(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	#return redirect(url_for('index')) #import 'redirect' and 'url_for' (top)
	
	total_predicted_time = 5 #in seconds
	return jsonify({'printing_time':total_predicted_time})

@app.route('/timeExceeded', methods = ['POST','GET'])
def time_exceeded():
	print("Printing time exceeded")
	return '' #returns an empty string (returns nothing)

@app.route('/stopPrinting', methods = ['POST','GET'])
def stop_event():
	print("Stop printer")
	return redirect(url_for('index'))



if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
