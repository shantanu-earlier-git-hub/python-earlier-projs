from flask import Blueprint
from main import db

test_bp = Blueprint('test', __name__)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)


@test_bp.route('/test')
def test():
    try:
        tests = db.session.execute(db.select(Test)).scalars().all()
        for test_db in tests:
            print(f" id {test_db.id} name {test_db.name}, age {test_db.age}")
    except BaseException as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()

    return 'test', 200
