from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "secret$Key"


@app.route("/")
def home():
    print("home called")
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    print("login called")
    email = request.form["email"]
    password = request.form["password"]
    print(email, password)
    return render_template("login.html", email=email)


if __name__ == "__main__":
    app.run(debug=True)
