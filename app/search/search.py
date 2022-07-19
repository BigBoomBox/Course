from flask import Blueprint, render_template, request
from utils import get_by_search

search_blueprint = Blueprint('search_blueprint', __name__, template_folder="tools")


@search_blueprint.route("/search")
def search_posts():
    s = str(request.args.get("s")).lower()
    search_list = get_by_search(s)
    posts_counter = len(search_list)
    return render_template("searched_list.html", search_list=search_list, search=s, counter=posts_counter)
