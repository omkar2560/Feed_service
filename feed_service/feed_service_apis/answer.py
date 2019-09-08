
from flask import request, jsonify
from flask_restful import Resource

from feed_service.feed_service_api_handler import answer_handler
from feed_service.utils.answer import get_answer_dict


class Answer(Resource):
    def post(self):
        data = request.get_json()
        answer_object = answer_handler.create_answer(data)
        response_dict = get_answer_dict(answer_object)
        response_json = jsonify({"answer": response_dict})
        return response_json

    def get(self):
        data = request.args
        answer_objects = answer_handler.get_answer(data)
        return jsonify({"answers": [get_answer_dict(x) for x in answer_objects]})

    def put(self):
        data = request.args
        answer_object = answer_handler.update_answer(data)
        return jsonify({"answer": get_answer_dict(answer_object)})



