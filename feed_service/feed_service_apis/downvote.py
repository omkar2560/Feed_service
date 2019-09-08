
from flask import request, jsonify
from flask_restful import Resource

from feed_service.feed_service_api_handler import downvote_handler
from feed_service.utils.downvote import get_downvote_dict


class Downvote(Resource):
    def post(self):
        data = request.get_json()
        upvote_object = downvote_handler.create_downvote(data)
        response_dict = get_downvote_dict(upvote_object)
        response_json = jsonify({"downvote": response_dict})
        return response_json

    def get(self):
        data = request.args
        downvote_objects = downvote_handler.get_downvote()
        return jsonify({"downvotes": [get_downvote_dict(x) for x in downvote_objects]})

    def put(self):
        data = request.args
        downvote_object = downvote_handler.update_downvote(data)
        return jsonify({"downvote": get_downvote_dict(downvote_object)})
