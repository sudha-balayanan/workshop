from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/star")
def star():
    return render_template("star.html")


@app.route("/game")
def game():
    return render_template("game.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4001, debug=True)
