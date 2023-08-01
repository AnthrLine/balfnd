from flask import Flask, render_template, send_file, request, make_response
import requests
import time
import uuid
import os
from threading import Thread
from modules import sheetoperator, mainhtmloperator, eqfsheetoperator, eqnfsheetoperator, indfsheetoperator, indnfsheetoperator, indpetsheetoperator, indgrsheetoperator, adgenerator, schedulef


app = Flask('app')
		
@app.route('/')
def main():
	return render_template("index.html")

@app.route('/sw.js')
def sw():
	return send_file("sw.js")

@app.route('/index')
def index():
	return render_template("index.html")

#@app.route('/testeqf')
def testeqf():
	eqfsheetoperator.exec()
	return ("Que sigui el que déu vulgui")

@app.route('/patrocinadors')
def patrocinadors():
	schedule.run_pending()
	return render_template("patrocinadors.html")

@app.route('/equipsfederats')
def equipsfederats():
	return render_template('eqf.html')

@app.route('/equipsnofederats')
def equipsnofederats():
	return render_template('eqnf.html')

@app.route('/individualnofederats')
def individualnofederats():
	return render_template('indnf.html')

@app.route('/individualfederats')
def individualfederats():
	return render_template('indf.html')

@app.route('/individual20102014')
def individual20102014():
	return render_template('indpet.html')

@app.route('/individual20062009')
def individual20062009():
	return render_template('indgr.html')

#@app.route('/csvexec')
def csvexec():
	sheetoperator.csvexec()
	indnfsheetoperator.exec()
	indfsheetoperator.exec()
	mainhtmloperator.exec()
	indpetsheetoperator.exec()
	indgrsheetoperator.exec()
	eqnfsheetoperator.exec()
	eqfsheetoperator.exec()
	return('Que sigui el que déu vulgui :)')

@app.route('/admin')
def admin():
	if request.cookies.get('uuid') == str(getuuid()):
		return render_template('admin.html')
	else:
		return loginform()

def getuuid():
	with open('uuid.txt', 'r') as uuidfile:
			uuidv = uuidfile.readlines()
			return(uuidv[0])

@app.route('/loginform')
def loginform():
	return render_template('loginform.html')
	
@app.route('/login', methods = ['POST', 'GET'])
def login():
	password = 'TESTPSWD'

	pwd = str(request.form.get('pwd'))

	if str(password) == str(pwd):
		uuidv = str(uuid.uuid4())

		with open('uuid.txt', 'w') as uuidfile:
			uuidfile.write(str(uuidv))

		resp = make_response(render_template('admin.html'))
		resp.set_cookie('uuid', uuidv)
		return resp 
	else:
		return loginform()
		

@app.route('/file', methods = ['POST', 'GET'])
def file():
	if os.path.exists('Web.xlsx'):
		os.remove('Web.xlsx')
	if request.cookies.get('uuid') == str(getuuid()):
		if request.method == 'POST':
			f = request.files['xlsx']
			f.save(f.filename)
			csvexec()
			return admin()	

	else:
		return("You don't have permission to do that")

@app.route('/nou')
def nou():
	return render_template("eqnfnou.html")

if __name__ == '__main__':
	# t = Thread(target=schedulef.run)
	# t.start()
	app.config['UPLOAD_FOLDER'] = '/'
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', port=5000)
	