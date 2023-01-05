from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Benton'},
        {'first_name' : 'John', 'last_name' : 'Johnson'},
        {'first_name' : 'Lee', 'last_name' : 'Loftiss'},
        {'first_name' : 'David', 'last_name' : 'Bowie'}
    ]
    return render_template("index.html", users = users)

if __name__=="__main__":
    app.run(debug=True, port=5001)
