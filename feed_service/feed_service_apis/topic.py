from flask import request, jsonify
from flask_restful import Resource

from feed_service.feed_service_api_handler import topic_handler
from feed_service.utils.topic import get_topic_dict


class Topic(Resource):
    def post(self):
        data = request.get_json()
        topic_object = topic_handler.create_topic(data)
        response_dict = get_topic_dict(topic_object)
        response_json = jsonify({"topic": response_dict})
        return response_json

    def get(self):
        data = request.args
        topic_objects = topic_handler.get_topic(data)
        return jsonify({"topics": [get_topic_dict(x) for x in topic_objects]})

    def put(self):
        data = request.args
        topic_object = topic_handler.update_topic(data)
        return jsonify({"topic": get_topic_dict(topic_object)})
