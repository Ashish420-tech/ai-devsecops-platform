from flask import Flask, jsonify

app = Flask(__name__)

# 1. Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "AI DevSecOps Platform is running 🚀"
    })

# 2. Health Check Route
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

# 3. Dummy API Endpoint
@app.route("/api/data")
def data():
    return jsonify({
        "data": "This is a dummy API response",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
