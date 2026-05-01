import random

from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from web_app.todo import todo_service
from web_app.todo.todo_model import TodoModel

todo_bp = Blueprint('todo_bp', __name__)


@todo_bp.route('/todo', methods=["GET"])
@todo_bp.route('/todo/all', methods=['GET'])
def fetch_all():
    todos = []
    todo_model_ = TodoModel(todo_id=0, title='', content='', status='', complete_date='')
    try:
        todos = todo_service.fetch_all()
    except BaseException as e:
        print('error', e)

    return render_template('todo/todo.html', todo_model=todo_model_, todos=todos)


@todo_bp.route('/todo/fetch/<todo_id>', methods=['GET'])
def fetch_by_id(todo_id=0):
    try:
        todo = todo_service.fetch_by_id(int(todo_id))
    except BaseException as e:
        print('error', e)

        return "no return data "
        # return render_template('todo/todo.html', todo_model=todo_model_, todos=todos)


@todo_bp.route('/todo/save/<todo_id>', methods=['POST'])
@todo_bp.route('/todo/update/<todo_id>', methods=['GET'])
def update_save(todo_id=0):
    pass


@todo_bp.route('/todo/delete/<todo_id>', methods=['GET'])
def delete(todo_id):
    print(f" id sent for delete the record -> {todo_id}")
    try:
        is_deleted = todo_service.delete(int(todo_id))
    except BaseException as e:
        print('error occurred during deleting record', e)

        return redirect('/todo/all')


@todo_bp.route('/todo/create', methods=['POST'])
def create():
    try:
        new_todo = TodoModel(
            todo_id=random.randint(1, 10000),
            title=request.form['title'],
            content=request.form['content'],
            status=request.form['status'],
            complete_date=request.form['complete_date']
        )
        generated_id = todo_service.create(new_todo)
        return redirect('/todo/all')
    except Exception as e:
        print('error occurred during creating new record', e)
