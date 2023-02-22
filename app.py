from flask import Flask

# Demo flask app 1st ml appp

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    return "Starting ML project"

if __name__ == "__main__":
    app.run(debug=True)
