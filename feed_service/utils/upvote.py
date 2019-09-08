from feed_service.utils.answer import get_answer_dict


def get_upvote_dict(upvote_object):
    return { "createdby": upvote_object.createdby,
            "answer": get_answer_dict(upvote_object.answer)
            }