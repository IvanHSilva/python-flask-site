from flask import Flask

app = Flask(__name__)

# first page

# route
@app.route("/")
def homepage():
    return "Home page site Flask"

if __name__ == "__main__":
    app.run(debug=True)
