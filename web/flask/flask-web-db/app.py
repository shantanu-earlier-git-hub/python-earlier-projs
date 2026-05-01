from flask import redirect

from main import app
from main.test import test_bp


@app.route('/')
def index():
    return redirect("/test")


if __name__ == '__main__':
    with app.app_context():
        app.register_blueprint(test_bp)
    app.run()
