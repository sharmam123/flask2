#! /usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Nix! Second App"

def run():
    app.run(host="0.0.0.0",port=5001)

if __name__ == "__main__":
    run()
