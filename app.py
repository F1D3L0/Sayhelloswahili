from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = 'qwerty12345'

@app.route('/hello')
def hello():
	flash('SAY YOUR NAME AND GET A SWAHILI GREETING!!')
	return render_template('index.html')

@app.route('/greet', methods=["POST","GET"])
def greet():
	flash('Why bother yourself '+str(request.form['name_input']) +', you already know it is jambo :)')
	flash('(JAMBO means Hello)')
	return render_template('index.html')
