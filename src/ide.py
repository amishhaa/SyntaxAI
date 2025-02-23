import ast
import sys
import io
import contextlib
from flask import Flask, render_template, request, jsonify
from mapmodule import MapModule 

app = Flask(__name__)
map_module = MapModule()  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    code = request.form['code']
    result = execute_code(code)
    return jsonify({'output': result})

@app.route('/predict', methods=['POST']) 
def predict():
    code = request.form['code']
    prediction = map_module.predict_snippet(code)
    return jsonify({'prediction': prediction})

def execute_code(code):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        exec(code)
    except Exception as e:
        return f"Error: {str(e)}"

    sys.stdout = sys.__stdout__  
    return captured_output.getvalue()

if __name__ == '__main__':
    app.run(debug=True)