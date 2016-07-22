from flask import (Flask, render_template, redirect,
                    url_for, request, make_response)
import json

app = Flask(__name__)

@app.route('/')
@app.route("/<name>")
def index(name="Buddy"):
    return render_template("index.html", name = name)
    # return "Hello {}!".format(name)

# default data type it comes in is a string!
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1,num2):
    context = {'num1': num1, "num2": num2}
    return render_template("add.html", **context)
    # return render_template("add.html", num1=num1, num2=num2)

# create the route for saving & uploading cookie data
@app.route('/save', methods=["POST"])
def save():
    # make the response
    response = make_response(redirect(url_for('index')))
    response.set_cookie("user", json.dumps(dict(request.form.items())))
    # response.set_cookie("character", json.dumps(data))
    # data = get_saved_data()
    # data.update(dict(request.form.items()))
    return response

# def get_saved_data():
#     try:
#         data = json.loads(request.cookies.get('user'))
#     except TypeError:
#         data = {}
#     return data

app.run(debug=True)
