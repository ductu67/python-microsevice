from flask import Flask, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify('Index Page')


@app.route("/hello", methods=['GET'])
def hello_microservice():
    message = {"message": "Hello from the microservice! This is Tund"}
    return jsonify(message)


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)
