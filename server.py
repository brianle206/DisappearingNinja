from flask import Flask, redirect, render_template, request, send_file, url_for
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/ninja')
def blue():
	return render_template("ninjas.html")

@app.route('/ninja/<ninja_color>')
def donatello(ninja_color):
	if ninja_color == 'blue':
		print "blue"
		return render_template("leonardo.html", ninja_color=ninja_color)
	elif ninja_color == 'orange':
		print "orange"
		return render_template("michelangelo.html", ninja_color=ninja_color)
	elif ninja_color == 'red':
		print "red"
		return render_template("ralphael.html", ninja_color=ninja_color)
	elif ninja_color == 'purple':
		print "purple"
		return render_template("donatello.html", ninja_color=ninja_color)
	else:
		print "anything else"
		return render_template("april.html", ninja_color=ninja_color)

app.run(debug=True)