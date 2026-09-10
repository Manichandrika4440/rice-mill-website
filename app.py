from flask import Flask, render_template

ricemill = Flask(__name__)

@ricemill.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    ricemill.run(debug=True)