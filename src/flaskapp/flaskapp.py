from flask import Flask
from square import getsquare

#main python flask handler
#calls a blueprint

app = Flask(__name__)
app.register_blueprint(getsquare)

@app.route("/")
def hello():
    return "Hello, this is a test!"
if __name__ == "__main__":
    app.run()
