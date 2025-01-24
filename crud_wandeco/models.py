from crud_wandeco import database


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True, nullable=False)
    name = database.Column(database.String(30), nullable=False)
    email = database.Column(database.String(20), nullable=False, unique=True)
    phone = database.Column(database.String(11), nullable=True)