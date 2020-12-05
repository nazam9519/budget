from flask import Flask,request,abort,jsonify
from square import getsquare
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.dialects.postgresql import JSON
import os,sys

app = Flask(__name__)
app.register_blueprint(getsquare)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nabil:1234@localhost/test_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
@app.route("/")
def hello():
    return "Hello World"


#from model import UserModel
@app.route('/testauth',methods=['POST','GET'])
def auth_handle():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = UserModel(username=data['username'],password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.username} has been created "}
        else:
            return {"error": "bad request"}
    elif request.method == 'GET':
        users = UserModel.query.all()
        results = [
            {
                "name": user.username,
                "password": user.password
            } for user in users]
        return {"count": len(results), "user": results}

class UserModel(db.Model):
    __tablename__ = 'loguser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text())
    password = db.Column(db.Text())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<name {}>'.format(self.username)
if __name__ == "__main__":
    app.run(debug=True)