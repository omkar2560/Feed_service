from feed_service.utils.topic import get_topic_dict


def get_question_dict(question_object):
    return {"q_string": question_object.q_string,
            "createdby": question_object.createdby,
            "createdon": question_object.createdon,
            "topic": get_topic_dict(question_object.topic),
            "id": question_object.id
            }