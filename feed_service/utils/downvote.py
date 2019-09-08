from feed_service.utils.answer import get_answer_dict


def get_downvote_dict(downvote_object):
    return { "createdby": downvote_object.createdby,
            "answer": get_answer_dict(downvote_object.answer)
            }