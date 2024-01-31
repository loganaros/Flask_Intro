from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

# Put your app in here.
@app.route("/<operation>")
def run_operation(operation):
    if operation == 'add':
        return f"{add(int(request.args['a']), int(request.args['b']))}"
    elif operation == 'sub':
        return f"{sub(int(request.args['a']), int(request.args['b']))}"
    elif operation == 'mult':
        return f"{mult(int(request.args['a']), int(request.args['b']))}"
    elif operation == 'div':
        return f"{div(int(request.args['a']), int(request.args['b']))}"
    else:
        return "not found"

@app.route("/math/<operation>")
def run_operation_aio(operation):
    if operation == 'add':
        return f"{add(int(request.args['a']), int(request.args['b']))}"
    elif operation == 'sub':
        return f"{sub(int(request.args['a']), int(request.args['b']))}"
    elif operation == 'mult':
        return f"{mult(int(request.args['a']), int(request.args['b']))}"
    elif operation == 'div':
        return f"{div(int(request.args['a']), int(request.args['b']))}"
    else:
        return "not found"