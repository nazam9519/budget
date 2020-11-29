from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.flaskapp.square import getsquare
from src.flaskapp.model import dbconn

#main python flask handler
#calls a blueprint

app = Flask(__name__)
app.register_blueprint(getsquare)
app.register_blueprint(model)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello, this is a test!"
if __name__ == "__main__":
    app.run()
