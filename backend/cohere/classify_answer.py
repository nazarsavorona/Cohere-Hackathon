import sys
import cohere

from backend.cohere.train_question import train_question

co = cohere.Client(sys.argv[1])


def classify_answer(question_id, answer):
    examples = train_question(question_id)

    inputs = [
        answer,
    ]

    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )

    return response
