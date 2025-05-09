from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to return "Hello World"
@app.route("/api/hello", methods = ["GET"])
def hello_world():
    response = {"message": "Hello World"}
    return jsonify(response)


# New route to sum two numbers
@app.route("/api/sum/<a>/<b>", methods = ["GET"])
def sum(a, b):
    c = int(a) + int(b)
    return jsonify({"sum":c})


if __name__ == "__main__":
    app.run()
