from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = "Kame Ha Me Ha"


# Have the root route ("/") show a page with the form
@app.route('/')
def index():
    return render_template("index.html")

# Have the "/result" route display the information from the form on a new HTML page
@app.route('/result')
def result():
    return render_template("result.html")


# Put the form data into session
@app.route('/posting', methods=['POST'])
def processing():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    session['food'] = request.form['food']
    session['allergy'] = request.form.getlist('allergy')
    session['comment'] = request.form['comment']
    return redirect('/result')

if __name__=="__main__":
    app.run(debug=True)