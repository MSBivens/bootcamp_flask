from flask import Flask
app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World!"

# Create a route that responds with "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
# Ensure the names provided in the 3rd task are strings
@app.route('/say/<name>')
def hi(name):
    print(name)
    return f"Hi {name}"

# Create a route that responds with the given word repeated as many times as specified in the URL
# For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output

# Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."
@app.route('/<oops>')
def oops(oops):
    print(oops)
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)