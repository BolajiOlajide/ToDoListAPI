from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config


app = Flask(__name__)
app.config.from_object(config['development'])

db = SQLAlchemy()

db.init_app(app)


@app.route('/')
def index():
    return 'App setup is nearing completion'


if __name__ == '__main__':
    app.run()
