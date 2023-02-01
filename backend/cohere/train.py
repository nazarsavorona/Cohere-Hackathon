import json
import sys
import cohere
from train_question import train_question
from backend.utils import write_to_file

co = cohere.Client(sys.argv[1])


def classify():
    examples, question = train_question(1)

    inputs = [
        "Global network",
        "Something interesting",
        "Communication using the same rules",
        "Conglomeration of networks",
        "Global system of interconnected computer networks"
    ]

    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )

    # TODO add question as top level of json structure, not separately
    output = json.dumps(question.__dict__, indent=4) + '\n'
    output += json.dumps(
        [response.classifications[i].__dict__ for i in range(len(response.classifications))],
        default=lambda o: '<not serializable>',
        indent=4
    )

    print(output)

    write_to_file.write_to_file("answers_1.txt", output)


classify()
