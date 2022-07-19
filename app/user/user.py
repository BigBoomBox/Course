from flask import Blueprint, render_template, request
from utils import get_users_posts

user_blueprint = Blueprint('user_blueprint', __name__, template_folder="templates")


@user_blueprint.route("/posts/<username>")
def users(username):
    user_posts = get_users_posts(username)
    user_name = user_posts[0]["poster_name"]
    return render_template('user-feed.html', users_posts=user_posts, user_name=user_name)
