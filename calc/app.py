# Put your app in here.
from flask import Flask, request, abort
import operations

app = Flask(__name__)

# Dictionary to map the operation names to functions
operations_dict = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

@app.route('/math/<operation>')
def do_math(operation):
    """Perform math operation based on the URL route parameter"""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    
    # Get the operation function from the dictionary
    operation_func = operations_dict.get(operation)
    
    if operation_func is None:
        abort(404, description="Invalid operation")

    # Perform the operation and return the result as a string
    result = operation_func(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)