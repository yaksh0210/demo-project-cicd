from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "DevOps Automation Platform",
        "status": "Running",
        "version": "1.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/metrics")
def metrics():
    return jsonify({
        "uptime": "running",
        "cpu": "normal"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
