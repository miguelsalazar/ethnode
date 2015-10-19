from app import app
from flask import jsonify, request, render_template, url_for

@app.route("/")
@app.route("/index")
@app.route("/index.htm")
@app.route("/index.html")
def index():
	return render_template("index.html")