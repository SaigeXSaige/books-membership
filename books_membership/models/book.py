from .base import db, BaseMixin

__all__ = ['Book']


class Book(BaseMixin, db.Model):
  
  __tablename__ = 'book'
  
  name = db.Column(db.Unicode(255), nullable=False)