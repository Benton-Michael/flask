from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="Super Secret"

# Have the root route render a template that displays the number of times the client has visited this site. 
# Refresh the page several times to ensure the counter is working.

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
        print('The index route was hit: Adding 1 to count')
    return render_template("index.html")

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/add_two')
def add_two():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
        print('The add_two route was hit: Adding 2 to count')
    return redirect("/") # adds another 1 to count when refreshed

# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
@app.route('/add_num', methods=["POST"])
def add_num():
    if "count" not in session:
        session["count"]=0
    else:
        num = request.form['num']
        session["count"] += int(num) -1
    return redirect("/")

#destroy_session route
@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5001)
    