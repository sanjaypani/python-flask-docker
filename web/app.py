from flask import Flask, request, jsonify

from flask_restful import Api, Resource

from pymongo import MongoClient

import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({'num_of_users': 0})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        logging.info("Previous Number is " + str(prev_num))
        new_num = prev_num + 1
        logging.info("Current Number is " + str(prev_num))
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello User " + str(new_num))

def checkPostedData(posted_data, function):
    if (function == 'add' or function == 'substract'  or function == 'multiply'):
        if 'a' not in posted_data or 'b' not in posted_data:
            return 301
        else:
            return 200

    elif function == 'division':
        if 'a' not in posted_data or 'b' not in posted_data:
            return 301
        elif int(posted_data['b']) == 0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = checkPostedData(posted_data, "add")

        if status_code != 200:
            retJson = {
            "message": "An Error occurred ...",
            "status_code": status_code
            }
            return jsonify(retJson)

        a = posted_data['a']
        b = posted_data['b']

        a = int(a)
        b = int(b)

        ret = a+b

        returnJson = {
            'Sum' : ret,
            'Status Code': 200
        }

        return jsonify(returnJson)

class Substract(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, "substract")

        if status_code != 200:
            retJson = {
            "message": "An Error occurred ...",
            "status_code": status_code
            }
            return jsonify(retJson)

        a = posted_data['a']
        b = posted_data['b']

        a = int(a)
        b = int(b)

        ret = a-b

        returnJson = {
            'Sum' : ret,
            'Status Code': 200
        }

        return jsonify(returnJson)

class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, "multiply")

        if status_code != 200:
            retJson = {
            "message": "An Error occurred ...",
            "status_code": status_code
            }
            return jsonify(retJson)

        a = posted_data['a']
        b = posted_data['b']

        a = int(a)
        b = int(b)

        ret = a*b

        returnJson = {
            'Sum' : ret,
            'Status Code': 200
        }

        return jsonify(returnJson)

class Divison(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = checkPostedData(posted_data, "division")

        if status_code != 200:
            retJson = {
            "message": "An Error occurred ...",
            "status_code": status_code
            }
            return jsonify(retJson)

        a = posted_data['a']
        b = posted_data['b']

        a = int(a)
        b = int(b)

        ret = (a*1.0)/b

        returnJson = {
            'Sum' : ret,
            'Status Code': 200
        }

        return jsonify(returnJson)

api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divison, "/division")
api.add_resource(Visit, "/hello")


@app.route('/')
def hello_world():
    return "Hello Sanjay !!!!!"

@app.route('/sum', methods=['POST'])
def sum():
    inputDict = request.get_json()
    a = inputDict['a']
    b = inputDict['b']

    c = a+b;

    response = {
    'Sum' : c
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
