from flask import Flask
from flask_alembic import Alembic

from books_membership.models import db
from books_membership.apis import api_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object('books_membership.config.settings')

    db.init_app(app)
    api_v1.init_app(app)
    Alembic(app)

    return app
