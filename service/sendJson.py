#!C:\Users\admte\AppData\Local\Programs\Python\Python310\python3.exe
import requests
import json

url = "http://localhost/Trabalho-DB-Python/service/service"
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)