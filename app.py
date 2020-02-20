from flask import Flask
import Schema

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    Schema()
    app.run(debug=True, port=80, host='0.0.0.0')