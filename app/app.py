from flask import Flask
from flask_cors import CORS
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(Configuration)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
