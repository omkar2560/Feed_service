from feed_service.db.feedservApp.models import Downvote, Answer


def create_downvote(data):
   answer_object = Answer.objects.get(id=data['answer'])
   downvote_object = Downvote.objects.create(answer=answer_object,createdby=data['createdby'])
   return downvote_object