from main import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship("Comment", backref=db.backref(
        "post", lazy=True))

    def __repr__(self):
        return f'<Post {self.id}: {self.title}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)

    def __repr__(self):
        return f'<Comment {self.id}>'
