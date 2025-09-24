from flask import Flask, jsonify, request

app = Flask(__name__)

# This is our first web endpoint. When the frontend asks for the
# home page, the server will respond with this message.
@app.route("/")
def home():
    return "Welcome to the Bingo App Backend!"

# This is a sample endpoint to make sure it's working.
# It returns a JSON object with a simple message.
@app.route("/api/status")
def status():
    return jsonify({"status": "Backend is running!"})

# To run the server, we'll use this block of code.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
