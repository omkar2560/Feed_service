'''
from flask import request, jsonify
from flask_restful import Resource

from feed_service.feed_service_api_handler import notification_handler
from feed_service.utils.notification import get_notification_dict


class Notification(Resource):
    def post(self):
        data = request.get_json()
        return notification_handler.create_notification()

    def get(self):
        data = request.args
        notification_objects = notification_handler.get_notification(data)
        return jsonify({"notifications": [get_notification_dict(x) for x in notification_objects]})

    def put(self):
        data = request.args
        notification_object = notification_handler.update_notification(data)
        return jsonify({"notification": get_notification_dict(notification_object)})
'''