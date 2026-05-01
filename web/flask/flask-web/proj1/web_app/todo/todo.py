from web_app import db


class Todo(db.Model):
    todo_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), default=False)
    complete_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Task {self.title}>"

    def __str__(self):
        return f" id: {self.todo_id}  title: {self.title} content: {self.content} status: {self.status} complete_date: {self.complete_date}"

    def __eq__(self, other):
        return ((self.todo_id == other.todo_id) and (self.title == other.title)
                and (self.content == other.content) and (self.status == other.status)
                and (self.complete_date == other.complete_date))

    def __hash__(self):
        return hash(self.todo_id)
