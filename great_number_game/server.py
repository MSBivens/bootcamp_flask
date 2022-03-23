from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key = "Wake up to reality!"

# In the root route, save a random number between 1 and 100 and display a form for the user to guess the number
@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

# Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
# Display the results as shown in the wireframe (i.e. with appropriate colors and positioning)
# Allow the user to keep guessing until they get it correct
@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

# Let the user know how many attempts they took before guessing the correct number
@app.route('/')
def guess_count():
    if "guess_count" not in session:
        session["guess_count"] = 0
    session["guess_count"] += 1
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)