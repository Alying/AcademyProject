from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
	return render_template('example_html.html')

#@app.route('/')
#def index():
#	return "Hello World!"
@app.route('/home')
def new_func():
	return render_template('you.html')

@app.route('/login')
def login():
	return render_template('login.html')
	
if __name__ == "__main__":
	app.run()