from flask import Flask, jsonify, render_template, request
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts", methods=["post"])
def posts():

    # Get start and end posts to generate.
    start = int(request.form.get("strart") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response.
    sleep(1)

    # Return list of posts.
    return jsonify(data)