"""App management settings defined here."""
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server

from app import create_app, db
from app.models import ToDoList

app = Flask(__name__)


app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """
    Create a context for interacting in a shell for the application.

    Import the model objects to enable easy interaction.
    """
    return dict(app=app, db=db, ToDoList=ToDoList)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
