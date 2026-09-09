import logging
import os
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.1.0")


@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return "Welcome to Enterprise CI/CD Pipeline!"


@app.route("/health")
def health():
    logger.info("Health endpoint accessed")
    return jsonify({
        "status": "UP"
    }), 200


@app.route("/version")
def version():
    logger.info("Version endpoint accessed")
    return jsonify({
        "version": APP_VERSION
    }), 200


@app.route("/info")
def info():
    logger.info("Info endpoint accessed")
    return jsonify({
        "application": "Enterprise CI/CD Pipeline",
        "version": APP_VERSION,
        "environment": os.getenv("ENVIRONMENT", "Development")
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)