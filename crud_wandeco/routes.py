from crud_wandeco import app
from flask import render_template, url_for, request, redirect
from crud_wandeco.models import Usuario
from crud_wandeco.forms import Form_create_user
from crud_wandeco import database

@app.route('/', methods=['GET', 'POST'])
def home():
    usuario = Usuario.query.all()
    formCreateUser = Form_create_user()
    if formCreateUser.validate_on_submit() and 'button_create' in request.form:
        create = Usuario(name=formCreateUser.name.data, email=formCreateUser.email.data, phone=formCreateUser.phone.data)
        database.session.add(create)
        database.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', usuario=usuario, formCreateUser=formCreateUser)

@app.route('/update')
def update():
    return render_template('home.html')

@app.route('/create', methods=['POST'])
def create():
    return render_template('home.html')
