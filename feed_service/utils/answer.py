from feed_service.utils.question import get_question_dict


def get_answer_dict(answer_object):
    return {"a_string": answer_object.a_string,
            "id": answer_object.id,
            "createdby": answer_object.createdby,
            "createdon": answer_object.createdon,
            "question": get_question_dict(answer_object.question)
            }