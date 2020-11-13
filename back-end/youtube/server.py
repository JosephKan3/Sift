from flask import Flask
from flask import request
from youtube import getCommentsByAuthorName
from flask import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return test()
    

@app.route('/channelByName/:channelName', methods = ['POST'])
def testing():
    channelName = request.args.get("channelName")
    print(dir(request.args))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(channelName)
    response = getCommentsByAuthorName(channelName)
    return response

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)