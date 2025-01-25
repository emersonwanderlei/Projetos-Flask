from crud_wandeco import app
from flask import render_template, url_for, request, redirect
from crud_wandeco.models import Usuario
from crud_wandeco.forms import Form_create_user
from crud_wandeco import database

@app.route('/', methods=['GET', 'POST'])
def home():
    usuario = Usuario.query.all()
    formCreateUser = Form_create_user()

    return render_template('home.html', usuario=usuario, formCreateUser=formCreateUser)

@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    user = Usuario.query.get(user_id)
    if user and 'button_update':
        database.session.add(user)
        database.session.commit()
        return redirect(url_for('home'))


    return redirect(url_for('home'))

@app.route('/create', methods=['POST'])
def create():
    formCreateUser = Form_create_user()
    if formCreateUser.validate_on_submit() and 'button_create' in request.form:
        create = Usuario(name=formCreateUser.name.data, email=formCreateUser.email.data, phone=formCreateUser.phone.data)
        database.session.add(create)
        database.session.commit()
        return redirect(url_for('home'))

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    user = Usuario.query.get(user_id)
    if user and 'button_delete':
        database.session.delete(user)
        database.session.commit()
    return redirect(url_for('home'))
