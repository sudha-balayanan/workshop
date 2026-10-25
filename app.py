from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

CHOICES = {"star", "game"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/choose")
def choose():
    choice = request.args.get("choice", "").strip().lower()
    if choice not in CHOICES:
        return render_template("index.html", error=f"Invalid choice: {choice!r}"), 400
    return redirect(url_for(choice))


@app.route("/star")
def star():
    return render_template("star.html")


@app.route("/game")
def game():
    return render_template("game.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4001, debug=True)
