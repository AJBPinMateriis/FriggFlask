from flask import Flask, render_template, redirect, url_for, request
import sys, os, time
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/pi/Desktop/Flask_Git/FriggFlask/uploaded_files'
#ALLOWED_EXTENSIONS = set(['txt']) #TRY LATER

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	className = "init_button"
	return render_template('index.html', color_class = className) #pass 'init_button' className to HTML tempalte using Jinja2
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
	#print(filename)
	f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	#print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
	elapsed_time()
	
	#return render_template('index.html') !DONT RENDER THE TEMPLATE, CALL THE FUNCTION WHICH DOES
	return redirect(url_for('index')) #import 'redirect' and 'url_for' (top)


#prints elapsed time
def elapsed_time():
	start_time = time.time()
	
	print(time.strftime("%H:%M:%S", time.gmtime(start_time))) #prints start time
	
	
	#time.sleep(5)
	#elapsed_time = time.time() - start_time #this gives me seconds elapsed, FIND A WAY to pass these seconds to HTML and format them
	
	for x in range(5):
		time.sleep(1)
		elapsed_time = time.time() - start_time
		print(int(elapsed_time))
		render_template('index.html', sec = elapsed_time)
		
	
	print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))) #prints elapsed time
	print(time.strftime("%H:%M:%S", time.gmtime(time.time())))  #prints final time

@app.route('/stopPrinting', methods = ['POST','GET'])
def stop_event():
	print("Stop printer")
	return redirect(url_for('index'))



if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
