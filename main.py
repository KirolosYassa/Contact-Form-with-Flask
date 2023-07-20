from flask import Flask, render_template, request
from LoginForm import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret$key$supersecret"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    print("home called")
    return render_template("index.html", form=LoginForm(), bootstrap=bootstrap)


@app.route("/login", methods=["GET", "POST"])
def login():
    print("login called")
    login_form = LoginForm()
    email = request.form["email"]
    password = request.form["password"]
    print(f"email: {email}\npassword: {password}")
    print(f"login_form.validate_on_submit() = {login_form.validate_on_submit()}")
    if login_form.validate_on_submit():
        print("Login successful")
        return render_template("success.html", bootstrap=bootstrap)

    print("Login failed")
    return render_template("denied.html", bootstrap=bootstrap)


if __name__ == "__main__":
    app.run(debug=True)
