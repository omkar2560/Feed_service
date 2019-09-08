from feed_service.db.feedservApp.models import Question, Topic


def get_question(data):
    question_objects = Question.objects.filter()
    return question_objects


def create_question(data):
    topic_object = Topic.objects.get(id=data['topic'])
    question_object = Question.objects.create(q_string=data['q_string'],
                                              topic=topic_object,
                                              createdby=data['createdby'])
    return question_object


