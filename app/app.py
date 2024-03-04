from flask import Flask, request

app = Flask(__name__)
last_msg = ''


@app.route('/')
def index():
    return "Hello"


@app.route('/reverse', methods=['GET'])
def reverse():
    if request.method == 'GET':
        input_string = request.args.get("in")
        output_string = reverse_sentence(input_string)
        return {"result": output_string}


@app.route('/restore', methods=['GET'])
def restore():
    if request.method == 'GET':
        return {
            "result": last_msg
        }


def reverse_sentence(sentence=''):
    global last_msg

    words = sentence.split(' ')
    reversed_sentence = ' '.join(reversed(words))
    last_msg = reversed_sentence
    return reversed_sentence


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
