from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Server Online"

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    print("收到数据:", data)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)