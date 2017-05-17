from flask import request
from flask_restful import Api
from flask_restful import Resource
from api.watson import Conversation

class Message(Resource):

    def post(self):

        cors_domains = "*"

        response_msg = {
            "msg": "",
            "error": False
        }

        try:
            req = request.json
            msg = req['message']
            watson_client = Conversation()
            res = watson_client.send_message(message=msg)

            if res['output']['text'].__len__() > 0:
                response_msg['msg'] = res['output']['text'][0]

            return response_msg, 200, {'Access-Control-Allow-Origin': cors_domains}

        except Exception as err:
            response_msg['msg'] = err.__str__()
            response_msg['error'] = True
            return response_msg, 400, {'Access-Control-Allow-Origin': cors_domains}
