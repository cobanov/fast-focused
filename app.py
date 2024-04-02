from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    with open("sucveceza.txt", "r") as file:
        text = file.read()

    words = text.split()  # Split the text into words
    return render_template("index.html", words=words)


if __name__ == "__main__":
    app.run(debug=True)
