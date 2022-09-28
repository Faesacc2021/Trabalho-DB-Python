#!C:\Users\admte\AppData\Local\Programs\Python\Python310\python3.exe
from flask import Flask, request
app = Flask(__name__)

@app.route('/service/', methods=['POST'])
def service():
    data = request.json()
    print(data)
  
app.run("http://localhost/service", debug=True)