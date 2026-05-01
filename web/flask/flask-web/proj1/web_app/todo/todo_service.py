import datetime

from web_app.todo.todo import Todo
from web_app.todo.todo_model import TodoModel
from web_app import db


def fetch_all() -> list[Todo] | BaseException:
    todos = list([])
    try:
        todo = Todo()
        todos = db.session.execute(db.select(Todo)).scalars().all()
    except BaseException as e:
        print('error occurred during fetching all records', e)
        db.session.rollback()
    finally:
        db.session.close()

    return todos


def fetch_by_id(id_: int) -> Todo | BaseException:
    try:
        todo = db.session.execute(db.select(Todo).filter_by(todo_id=id_)).scalar_one_or_none()
    except BaseException as e:
        print(f'error occurred during fetching record by id {id_,} exception is {e}')
        db.session.rollback()
    finally:
        db.session.close()

    return todo


def create(todo: TodoModel) -> int | BaseException:
    todo_db = Todo()
    try:
        todo_db.todo_id = todo.todo_id
        todo_db.title = todo.title
        todo_db.content = todo.content
        todo_db.status = todo.status
        # todo_db.complete_date = datetime.datetime.strptime(todo.complete_date, '%m/%d/%Y')
        todo_db.complete_date = datetime.datetime.strptime(todo.complete_date, '%Y-%m-%d')
        db.session.add(instance=todo_db)
        db.session.commit()
        print(f"created  id in service {todo_db.todo_id}")
    except (ValueError, BaseException) as e:
        print('add service error', e)
        db.session.rollback()
    finally:
        db.session.close()

    return todo_db.todo_id


def update(updated_todo: Todo) -> bool | BaseException:
    id_ = updated_todo.todo_id
    old_todo = fetch_by_id(id_)
    if not old_todo.__eq__(updated_todo):
        try:
            db.session.merge(updated_todo)
            db.session.commit()
            return True
        except BaseException as e:
            print('error occurred during updating the record', e)
            db.session.rollback()
            return e
        finally:
            db.session.close()
    else:
        return False


def update_many(updated_todo: list[Todo]) -> bool | Exception:
    pass


def delete(id_: int) -> bool | BaseException:
    is_deleted = bool(0)
    try:
        todo = fetch_by_id(id_)
        print(f"deleting record .... -> {todo.title}")
        is_deleted = db.session.delete(todo)
        db.session.commit()
    except BaseException as e:
        print('error occurred during deleting the record', e)
        db.session.rollback()
    finally:
        db.session.close()
        return is_deleted


def delete_many(self, ids: list[int]) -> bool | Exception:
    pass
