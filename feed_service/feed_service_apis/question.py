from flask import request, jsonify
from flask_restful import Resource

from feed_service.feed_service_api_handler import question_handler
from feed_service.utils.question import get_question_dict


class Question(Resource):
    def post(self):
        data = request.get_json()
        question_object = question_handler.create_question(data)
        response_dict = get_question_dict(question_object)
        response_json = jsonify({"question":response_dict})
        return response_json

    def get(self):
        data = request.args
        question_objects = question_handler.get_question(data)
        return jsonify({"questions": [get_question_dict(x) for x in question_objects]})

    def put(self):
        data = request.args
        question_object = question_handler.update_question(data)
        return jsonify({"question": get_question_dict(question_object)})
