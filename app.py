import flask
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    #return "My first server message"
    return render_template('index.html')

@app.route("/next")
def next():
    #return "My first server message"
    return render_template('next.html',name = "anamika")


app.run(debug=True )

