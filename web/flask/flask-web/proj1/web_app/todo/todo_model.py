from dataclasses import dataclass


@dataclass
class TodoModel:

    def __init__(self, todo_id=None, title='', content='', status='', complete_date=None):
        self.todo_id = todo_id
        self.title = title
        self.content = content
        self.status = status
        self.complete_date = complete_date

    def __repr__(self):
        return f"<Task {self.title}>"

    def __str__(self):
        return f" id: {self.id_}  title: {self.title} content: {self.content} status: {self.status} complete_date: {self.complete_date}"

    def __dict__(self):
        return self.__dict__
