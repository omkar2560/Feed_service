from feed_service.db.feedservApp.models import Answer, Upvote


def create_upvote(data):
   answer_object = Answer.objects.get(id=data['answer'])
   upvote_object = Upvote.objects.create(answer=answer_object,createdby=data['createdby'])
   return upvote_object
