from flask import redirect, url_for
from main import app, db
from main.login.login_routes import login_routes
from main.posts.posts_routes import post_bp

all_blueprints = [post_bp, login_routes]


@app.route('/')
def index():
    return redirect(url_for('login_routes.predict'))


if __name__ == '__main__':

    for blue_print in all_blueprints:
        app.register_blueprint(blue_print)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
