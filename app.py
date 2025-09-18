#Naredimo strežnik

from flask import Flask, render_template, request
import random
#pip install flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/CalcLove")
def calc():
    print(request.args)
    req = request.args
    ime1 = req.get("ime1")
    ime2 = req.get("ime2")
    rnd=random.randint(0,100)
    rez=f"{ime1} in {ime2} se imata rada {rnd}%"
    if {ime1}=="Beno" or {ime2}=="Beno":
        print("Beno je zakon")
    else:
        return render_template("index.html", rezultat=rez)

app.run(debug = True)