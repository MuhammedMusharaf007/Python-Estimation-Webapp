#main.py
from flask import Flask, request, render_template
import estimators

app= Flask(__name__)


@app.route("/") #decorator
def hello():
	return render_template("index.html")

													
@app.route("/estimate", methods=["POST"])
def estimate():
	algorithm = request.form['algorithm']
	iterations = request.form['iterations']
	if algorithm =='mc':
		estimate = estimators.estimate_mc(int(iterations))
	elif algorithm =='wallis':
		estimate = estimators.estimate_wallis(int(iterations))
	names = {	'mc':'Monte Carlo estimation',
						'wallis' : 'Wallis Product estimation'}
	return render_template("estimate.html",
												algorithm = names[algorithm],
												iters = iterations,
												estimate = estimate)