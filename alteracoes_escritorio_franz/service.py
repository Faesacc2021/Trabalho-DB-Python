from json import dump
import json
from flask import Flask, request
from flask import jsonify
from requests import Response
app = Flask(__name__)

@app.route('/include', methods=['GET','POST'])
def include():
    data = request.json
    print("Include")
    return json.dumps(data)

@app.route('/update', methods=['GET','POST'])
def update():
    data = request.json
    print("Update")
    return json.dumps(data)
  
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False, threaded=True)