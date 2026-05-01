from web_app import db, app
from web_app.routes import routes_bp
from web_app.todo import todo_bp

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.register_blueprint(routes_bp)
        app.register_blueprint(todo_bp)

        # print("Database tables created!")
    app.run(host='0.0.0.0', port=8080)
