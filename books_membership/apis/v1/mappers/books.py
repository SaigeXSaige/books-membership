from kim import field

from .base import BaseMapper

from books_membership.models import Book


class BookMapper(BaseMapper):

    __type__ = Book

    name = field.String()