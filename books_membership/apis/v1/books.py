
from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin

from books_membership.models import db, Book
from .mappers import BookMapper

books_resource = Resource('books', __name__, url_prefix='/books')


class BooksIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):

    name = 'list'
    many = True
    mapper_class = BookMapper
    model = Book

    def get_query(self):

        stmt = db.session.query(Book)
        return stmt


books_resource.add_endpoint(BooksIndexEndpoint)