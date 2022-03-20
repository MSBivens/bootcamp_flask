# Have the css in a separate stylesheet and link this to the template

from flask import Flask, render_template
app = Flask(__name__)

# Have the root route render a template with a checkerboard on it
@app.route('/')
def checkerboard():
    return render_template("index.html",row=8,col=8,color_one='red',color_two='black')

# Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
@app.route('/<int:x>')
def row(x):
    return render_template("index.html",row=x,col=8,color_one='red',color_two='black')

# Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route('/<int:x>/<int:y>')
def rowcol(x,y):
    return render_template("index.html",row=x,col=y,color_one='red',color_two='black')

# Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>/')
def rowcolcolor(x,y,color1,color2):
    return render_template("index.html",row=x,col=y,color_one=color1,color_two=color2)


if __name__ == "__main__":
    app.run(debug=True)