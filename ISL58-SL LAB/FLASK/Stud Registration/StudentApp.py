from flask import Flask, redirect, render_template, request, url_for
import time #time and date related functions
import re  #regular expressions

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def indexJS():
	if request.method == "GET":
		msg="***hello user enter your details***"
		return render_template("indexJS.html",msg=msg)

	if request.method == "POST":

		#Check if form fields are empty
		if request.form["usn"] == "" or request.form["dob"] == "" :
			msg = "***All form fields are required***"
			return render_template("indexJS.html", msg=msg)

		#Check if date entered in dd/mm/yyyy format and is not an invalid date Eg. 31/11/2016
		#Use strptime() function which raises an exception if date is invalid
		try:
			time.strptime(request.form["dob"],"%d/%m/%Y")
		except ValueError:
			msg = "***Date is invalid***"
			return render_template("indexJS.html", msg=msg)

		#Regex for USN
		usn_pattern = "^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"

		#Check if entered USN matches Regex
		if not re.match(usn_pattern, request.form["usn"]) :
			msg = "***USN format invalid***"
			return render_template("indexJS.html", msg=msg)

		#If form fields are valid return success HTML page
		l=[request.form["usn"],request.form["dob"]]
		return render_template("success.html", l=l)

if __name__ == '__main__':
	app.run()
	# app.run(host='192.168.43.177', port='8000', debug=True)
