import django;
from flask import Flask

django.setup()

from feed_service.feed_service_apis.topic import Topic
from feed_service.feed_service_apis.question import Question
from feed_service.feed_service_apis.answer import Answer
from feed_service.feed_service_apis.upvote import Upvote

from feed_service.feed_service_apis.downvote import Downvote
'''from feed_service.feed_service_apis.notification import Notification'''

from flask_restful import Api

app = Flask(__name__)

api = Api(app)

api.add_resource(Topic, '/topic', '/topic<name>')
api.add_resource(Question, '/question', '/question')
api.add_resource(Answer, '/answer', '/answer')
api.add_resource(Upvote, '/upvote', '/upvote')

api.add_resource(Downvote, '/downvote', '/downvote')
'''api.add_resource(Notification, '/notification', '/notification')'''

if __name__ == '__main__':
    app.run(host='localhost', port=2004, debug=True)
