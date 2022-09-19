import random

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/example')
def example():
    return ''.join(f'<p>{random.randint(0, 100)}</p>' for _ in range(20))

@app.route('/greetings/<name>/<int:age>')
def greetings_by_path(name: str, age: int):
    return f'Hi, {name}. You are {age} old.'

@app.route('/greetings-2')
@use_args({"name": fields.Str(required=True), 'age': fields.Int(required=True)}, location="query")
def greetings_by_query(args):
    name = args["name"]
    age = args["age"]


    return f'Hi, {name}. You are {age} old.'

if __name__ == '__main__':
    app.run()

