from flask import Blueprint, jsonify
from main import db
from main.login import User, Test
from main.models import get_predictions

login_routes = Blueprint('login_routes', __name__)


@login_routes.route('/users')
def users():
    user = User();
    user.username = 'some user'
    user.password = ''
    return jsonify(user.serialize(), 200)


@login_routes.route('/test')
def test():
    try:
        tests = db.session.execute(db.select(Test)).scalars().all()
        tests_json = [item.serialize() for item in tests]
        response = jsonify({"tests": tests_json}, 200, 'fetched data successfully')
    except BaseException as e:
        response = jsonify({"error": str(e)}, 500, 'error occured')
        db.session.rollback()
    finally:
        db.session.close()

    return response


@login_routes.route('/predict')
def predict():
    try:
        camp = [[150, 21, 9]]
        prediction = get_predictions(camp)
        response = jsonify({"data": prediction}, 200, 'fetched data successfully')
        return response
    except BaseException as e:
        response = jsonify({"error": str(e)}, 500, 'error occured')
        return response
