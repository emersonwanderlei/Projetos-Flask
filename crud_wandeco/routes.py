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

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = Usuario.query.get(user_id)
    if not user:
        return redirect(url_for('home'))
    formCreateUser = Form_create_user()
    if user and 'button_update':
        formCreateUser.name.data = user.name
        formCreateUser.email.data = user.email
        formCreateUser.phone.data = user.phone

    usuarios = Usuario.query.all()
    return render_template('home.html', usuario=usuarios, formCreateUser=formCreateUser, editing=True, user_id=user_id)


@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    user = Usuario.query.get(user_id)
    if not user:
        return redirect(url_for('home'))
    
    formCreateUser = Form_create_user()
    if formCreateUser.validate_on_submit():
        user.name = formCreateUser.name.data
        user.email = formCreateUser.email.data
        user.phone = formCreateUser.phone.data

        database.session.commit()
    return redirect(url_for('home'))
