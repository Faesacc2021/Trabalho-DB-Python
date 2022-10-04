import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from LoginUser import LoginUser
from createLoginUser import CreateLoginUser

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/serviceUm', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def serviceUm():
    data = json.dumps(request.json)
    data2 = json.loads(data)
    loginUser = LoginUser(**data2)
    responseCreateLogin = CreateLoginUser.createLogin(loginUser)
    returnJson = json.dumps(responseCreateLogin.__dict__)
    return returnJson
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)