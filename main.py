from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    print("home called")
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    print("login called")
    name = request.form["name"]
    password = request.form["password"]
    print(name, password)
    return render_template("login.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
