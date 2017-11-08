from flask import Flask, flash, redirect, render_template, request, session, abort, Response


app = Flask(__name__)

@app.route('/')
def home():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
