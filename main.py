from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    print("home called")
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def get_data():
    print("get_data called")
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
