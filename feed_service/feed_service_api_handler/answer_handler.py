
from flask import jsonify

from feed_service.db.feedservApp.models import Question, Answer


def create_answer(data):
   question_object = Question.objects.get(id=data['question'])
   answer_object = Answer.objects.create(a_string=data['a_string'],
                                          question=question_object,
                                          createdby=data['createdby']
                                          )
   question_object.answer.add(answer_object)
   return answer_object


def get_answer(data):
    answer_objects = Answer.objects.filter()
    return answer_objects
