from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return "About what?"


@app.route("/somepage/")
def somepage():
    return render_template("somepage.html")


@app.route("/result", methods=["GET"])
def handle_data():
        first_name = request.args.get("first_name", None)
        last_name = request.args.get("last_name", None)

        if not any((first_name, last_name)):
            return "Why didn't you insert your name? Don't you trust me? :("
        else:
            return "Hello, "\
                   + first_name\
                   + " "\
                   + last_name\
                   + "!"


if __name__ == "__main__":
    app.debug = True
    app.run()
