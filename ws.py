from flask import Flask, request, jsonify
from flask_restful import Api
import json
from dicttoxml import dicttoxml

app = Flask(__name__)

api=Api(app)

@app.route('/add',methods=['POST'])
def Addition():
    posted = request.args
    x = posted["x"]
    y = posted["y"]
    x = int(x)
    y = int(y)
    s = x + y
    ret = {'valeur1':x,'valeur2':y,'somme':s}
    return jsonify(ret)

@app.route('/diff',methods=['POST'])
def difference():
    posted = request.args
    x = posted["x"]
    y = posted["y"]
    x = int(x)
    y = int(y)
    res = x-y
    ret = {'valeur1':x,'valeur2':y,'difference':res}

    return jsonify(ret)
@app.route('/multi',methods=['POST'])
def Multiplication():
    posted = request.args
    x = posted["x"]
    y = posted["y"]
    x = int(x)
    y = int(y)
    res = x*y
    ret = {'valeur1':x,'valeur2':y,'multiplication':res}
    return dicttoxml(ret)#ret_xml

@app.route('/div',methods=['POST'])
def Division():
    posted = request.args
    x = posted['x']
    y = posted['y']
    x = int(x)
    y = int(y)
    quo = x*1.0/ y
    ret = {
        'dividende':x,
        'diviseur':y,
        'quotient':quo
    }
    #ret_xml = 
    return dicttoxml(ret)#ret_xml
@app.route("/", methods=["GET"])
def Home():
        return {"statut":"Bienvenue Mon Service Web"}
api.representations['application/xml'] = Division
api.representations['application/xml'] = Multiplication

if __name__ == "__main__":
    app.run(debug=True)