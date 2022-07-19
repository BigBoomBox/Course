import json


def get_posts():
    with open("tools/data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_users_posts(user_post):
    user_posts = []
    data = get_posts()
    for i in data:
        if i["poster_name"] in user_post:
            user_posts.append(i)
    return user_posts


def get_comments_by_post_id(pk):
    user_comments = []
    with open("tools/data/comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    for i in comments:
        if i["post_id"] in pk:
            user_comments.append(i)
    return user_comments


def get_by_search(search):
    data = get_posts()
    result = []
    for i in data:
        if search.lower() in i["content"]:
            result.append(i)
    return result


def get_posts_by_pk(pk):
    data = get_posts()
    for i in data:
        if i["pk"] in pk:
            posts = i
            return posts

