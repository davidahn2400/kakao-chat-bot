from flask import Flask, request
import sys


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/name", methods=["POST"])
def name_function():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": {
                "simpleText": {
                    "text": "안녕하세요."
                }
            }
        }
    }
    return responseBody

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(sys.argv[1]), debug=True)
