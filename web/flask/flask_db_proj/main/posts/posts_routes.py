from flask import Blueprint, request
from main import db

from main.posts import Post, Comment

post_bp = Blueprint('posts_bp', __name__)


def create_post(post):
    post = Post(title=post.title)
    try:
        db.session.add(post)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    finally:
        db.session.close()


@post_bp.route('/posts/all', methods=['GET'])
def get_pots():
    return "reached posts route"


@post_bp.route('/posts/create', methods=['GET', 'POST'])
def create_post(post):
    if request.method == 'GET':
        create_post(post)

    return "created post"
