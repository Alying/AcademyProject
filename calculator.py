from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return "Hello World!"

@app.route('/add/<x>/<y>')
def add(x, y):
	try:
		
		return str(int(x)+int(y))
	except:
		return "Error."

@app.route('/divide/<x>/<y>')
def divide(x, y):
	return str(x/y)

@app.route('/subtract/<x>/<y>')
def subtract(x, y):
	return str(int(x)-int(y))

@app.route('/multiply/<x>/<y>')
def multiply(x, y):
	return int(x)*int(y)

if __name__ == "__main__":
	app.run()