from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello World!"

@app.route('/test', methods =['GET'])
def test():
    if request.method == "GET":
        return jsonify({"message": "Hello, World!"})
    
if __name__ == '__main__':
    app.run(debug=True)