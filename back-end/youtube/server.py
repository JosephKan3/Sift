from flask import Flask
from flask import request
from youtube import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return test()
    

@app.route('/channelByName', methods = ['POST'])
def testing():
    if request.method == "POST":
        channelName = request.args.get('channelName')
        return getCommentsByAuthorName(channelName)

if __name__ == "__main__":
    app.run(debug=True, port=5000)