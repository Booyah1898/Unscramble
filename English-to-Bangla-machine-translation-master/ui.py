from flask import Flask,render_template,url_for,flash,redirect,request
import translator
from form import Enter

import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f1324e414f9dcd52971f749021a21ddd'

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/reference')
def intro():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/examples')
def examples():
	
	outeng,outban,lenout=translator.final()
	
	
	print('working properly call function')
	return render_template('examples.html',outeng=outeng,outban=outban,lenout=lenout)

@app.route('/test',methods=['GET','POST'])
def test():
	form = Enter(request.form)
	if request.method=='POST' and form.validate():
		sentence = str(form.sentence.data)
		workingDir = os.getcwd()

		model_file = workingDir + '/data/Translation_model.txt'
		with open(model_file, 'r') as f:
			model = json.load(f)
		outStr = ' '
		tokens = translator.tokenize(sentence)
		translated_tokens = translator.translate(tokens, model)
		outStr = outStr.join(translated_tokens)
		print(outStr)
		return render_template('test.html',output=outStr,form=form)
	return render_template('test.html',form=form)
if __name__=="__main__":
	app.run(debug=True)
