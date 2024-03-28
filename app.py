from flask import Falsk,render_template,request
import requests
app = Flask(__name__)
@app.route("/")
def main():
	return render_template("index.html")
@app.rout('/',methods = ['POST'])
def math_operations():
	e = request.form['text']
	o = request.form['operation']
	r = 'https://newton.now.sh/api/v2//'+o+'/'+e
	d = requests.get(r).json()
	a = d['result']
	return render_template('index.html',result = a,equation = e)
if __name__=="__main__":
	app.run()