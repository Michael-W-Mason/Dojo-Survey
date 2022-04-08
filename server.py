from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "asd;fiujashbdvpoiadbv"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html", name = session['name'], loc = session['location'], lang = session['lang'], comment = session['comment'])

@app.route("/main", methods=["POST"])
def main():
    session.clear()
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)