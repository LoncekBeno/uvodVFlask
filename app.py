#Naredimo strežnik

from flask import Flask, render_template
#pip install flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/CalcLove")
def calc():
    print("Calculating love...")
    return render_template("index.html")

app.run(debug = True)