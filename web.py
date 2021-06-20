from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def epGet():

    return "<h1>Hello World !!! na nuvem do Heroku.</h1>"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
