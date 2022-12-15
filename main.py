import flask
from views import views_users, views_books

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
    return "<h1>Démo CESI</h1><p>Solution d'authentification via web services</p>"

app.add_url_rule('/rest/register/user', methods=['POST'], view_func=views_users.register_user)
app.add_url_rule('/rest/auth/user', methods=['POST'], view_func=views_users.auth_user)
app.add_url_rule('/rest/get/books', methods=['GET'], view_func=views_books.get_books)


if __name__ == "__main__":
    app.run(host='0.0.0.0')