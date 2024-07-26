import flask
from flask import Flask,render_template,jsonify,request
from data import students
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "data":students,
        "message":"success"
    }),200
    
    
#http://127.0.0.1:5000/student?name=Pravalika
@app.route("/student")
def student():
    sname = request.args.get("name")
    for item in students:
        if sname == item["name"]:
            return jsonify({
                "data":item,
                "message":"success"
            }),200


app.run(debug=True )
