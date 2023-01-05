# pipenv install flask

# pipenv shell  ---> enter the virtual env

# start the server --> Python3 server.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

# assigning the route endpoints
# these are GET requests
@app.route('/dojo')
def dojo():
    return "Dojo!"

# create one URL Pattern and Function that can handle the following examples:
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}"

# remember: every variable that goes through the URL becomes a string
# so when it get's passed into the function it is a str

# cast it in the URL
@app.route('/repeat/<int:number>/<string:word>')
def repeat_word(number, word):
    # place each word on a new line
    output = ''

    for i in range(0, number):
        output += f"<p>{word}</p>"

    return output
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)