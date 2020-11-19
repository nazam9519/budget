from flask import Flask, request, abort, jsonify, Blueprint

#taken from  flask post example found on MEDIUM
#11/18/2020 customized to work with apache2 and blueprint

getsquare = Blueprint('getsquare',__name__)


@getsquare.route('/getSquare', methods=['POST'])
def get_square():
    if not request.json or 'number' not in request.json:
        abort(400)
    num = request.json['number']

    return jsonify({'answer': num ** 2})
