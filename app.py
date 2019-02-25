from flask import Flask, render_template, redirect, url_for, request
import sys

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	#variable = request.form
	#return(sys.version) SHOWS PYTHON VERSION
	
@app.route('/getData', methods = ['POST','GET'])#if 'methods' is not declared, the default is GET
def get_event():
	print("Initialize printer")
	
	#result = request.form['texto']
	result = request.args.get('texto')
	print(result)
	
	#return render_template('index.html') !DONT RENDER THE TEMPLATE, CALL THE FUNCTION WHICH DOES
	return redirect(url_for('index')) #import 'redirect' and 'url_for' (top)

@app.route('/stopPrinting', methods = ['POST','GET'])
def stop_event():
	print("Stop printer")
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
