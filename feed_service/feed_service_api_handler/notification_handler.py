'''
from flask import jsonify

from feed_service.feed_service_apis import notification
from feed_service.feed_service_apis.notification import Notification


def question_object():
    pass


def get_notification_dict():
    pass


def create_notification():
    notification_object = Notification.objects.get(notification)
    return jsonify({"notification": get_notification_dict()})
'''