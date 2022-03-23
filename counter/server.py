from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key = "Kame Ha Me Ha"

# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template("index.html")

# Add a Reset button to reset the counter
# Add a "/destroy_session" route that clears the session and redirects to the root route.
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

# Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/double')
def double():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 2
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)