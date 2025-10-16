from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/ip")
def get_ip():
    ip = request.remote_addr
    return f"Your IP is {ip}"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)
    return {"received": data}, 200

# Entry point for Cloud Run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)