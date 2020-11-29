from src.flaskapp.flaskapp import db 
from sqlalchemy.dialects.postgresql import JSON
from flask import Flask,request,abort,jsonify,Blueprint

dbconn = Blueprint('testauth',__name__)
class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, user, password):
        self.user = username
        self.password = password

    def __repr__(self):
        return '<name {}>'.format(self.username)


@dbconn.route('/testauth',methods=['POST','GET'])
def auth_handle():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = UserModel(name=data['username'],password=data['password'])
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
        return {"count": len(results), "cars": results}