
from flask import request, jsonify
from flask_restful import Resource

from feed_service.feed_service_api_handler import upvote_handler
from feed_service.utils.upvote import get_upvote_dict


class Upvote(Resource):
    def post(self):
        data = request.get_json()
        upvote_object = upvote_handler.create_upvote(data)
        response_dict = get_upvote_dict(upvote_object)
        response_json = jsonify({"upvote": response_dict})
        return response_json

    def get(self):
        data = request.args
        upvote_objects = upvote_handler.get_upvote(data)
        return jsonify({"upvotes": [get_upvote_dict(x) for x in upvote_objects]})

    def put(self):
        data = request.args
        upvote_object = upvote_handler.update_upvote(data)
        return jsonify({"upvote": get_upvote_dict(upvote_object)})
