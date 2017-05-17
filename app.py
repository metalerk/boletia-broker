from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource
from api.messages import Message
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, methods=["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"])

api.add_resource(Message, '/message')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
