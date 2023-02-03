from backend.cohere.classify_answer import classify_answer


def assess_answer(question_id, answer):
    return classify_answer(question_id, answer)