from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/<name>")
def index(name="Buddy"):
    return "Hello {}!".format(name)

# default data type it comes in is a string!
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1,num2):
    return "{} + {} = {}".format(num1, num2, num1+num2)

# @app.route('/multiply')
# @app.route('/multiply/<int:num1>/<int:num2>')
# @app.route('/multiply/<float:num1>/<float:num2>')
# @app.route('/multiply/<int:num1>/<float:num2>')
# @app.route('/multiply/<float:num1>/<int:num2>')
# def multiply(num1=5, num2=5):
#     return "{} *{} = {}".format(num1, num2, num1*num2)
@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
def multiply(num1=5, num2=5):
    return str(num1*num2)

app.run(debug=True)
