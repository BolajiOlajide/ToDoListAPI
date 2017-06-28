"""
Define SQLAlchemy models.

The SQLAlchemy models for the database is defined here.
"""

from datetime import datetime

from . import db


class CRUDMixin(object):
    """
    Define the Create,Read, Update, Delete mixin.

    Instantiate a mixin to handle save, delete and also handle common model
    columns and methods.
    """

    date_created = db.Column(
        db.DateTime, default=datetime.now(), nullable=False)

    def save(self):
        """
        Save to database.

        Save instance of the object to database and commit.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete from database.

        Deletes instance of an object from database
        """
        db.session.delete(self)
        db.session.commit()


class ToDoList(CRUDMixin, db.Model):
    """
    Set up the ToDoList model.

    Define the properties of the ToDoList model and the table name too.
    """

    __tablename__ = 'todoList'
    todoList_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Display the string representation of the ToDoList model."""
        return '<ToDoList: {}>'.format(self.name)
