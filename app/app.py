from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello DevOps! Version 1.0\n"


@app.route("/health")
def health():
    return "OK\n"


@app.route("/info")
def info():
    return {
        "application": "hello-devops",
        "version": os.getenv("APP_VERSION", "1.0")
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
