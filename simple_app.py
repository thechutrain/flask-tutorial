from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Buddy"):
    name = request.args.get("name", name)
    return "Hello {}!".format(name)

app.run(debug=True)
