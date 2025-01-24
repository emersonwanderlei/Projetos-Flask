from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '12345679-75'


csrf = CSRFProtect(app)

database = SQLAlchemy(app)
app.app_context().push()

from crud_wandeco import routes