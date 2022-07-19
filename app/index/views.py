from flask import Blueprint, render_template, request
from utils import get_posts, get_comments_by_post_id, get_posts_by_pk


index_blueprint = Blueprint('index_blueprint', __name__, template_folder="tools")


@index_blueprint.route("/")
def index():
    list_data = get_posts()
    return render_template('index.html', content=list_data)


@index_blueprint.route("/posts/<int:post_id>")
def get_posts(post_id):
    comments = get_comments_by_post_id(post_id)
    post = get_posts_by_pk(post_id)
    len_list = len(comments)
    return render_template('post.html', post_info=post, list_comments=comments, len_list=len_list)
