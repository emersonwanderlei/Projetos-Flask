from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

class Form_create_user(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Contato', validators=[DataRequired()])
    button_create = SubmitField('Adicionar')
    button_update = SubmitField('Editar')
    button_delete = SubmitField('Deletar')