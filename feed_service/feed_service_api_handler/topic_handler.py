import user

from flask import jsonify

from feed_service.db.feedservApp.models import Topic


def get_topic(filters):
    if 'name' in filters:
        topic_objects = Topic.objects.filter(users=filters['name'])
    else:
        topic_objects = Topic.objects.all()
    return topic_objects


def create_topic(data):
    topic_object = Topic.objects.create(name=data['name'], users=data['users'])
    return topic_object
