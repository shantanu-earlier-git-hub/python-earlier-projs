from flask import Blueprint, render_template

routes_bp = Blueprint('routes_bp', __name__)


@routes_bp.route('/', methods=['GET'])
@routes_bp.route('/home', methods=['GET'])
def home():
    return render_template('home/home.html')


@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')

# @routes_bp.route('/todo', methods=['GET'])
# def todo():
#     todo_model = TodoModel(todo_id=0, title='', content='', status='', complete_date='')
#     todos = todo_service.fetch_all()
#     return render_template('todo/todo.html', todo_model=todo_model, todos=todos)
