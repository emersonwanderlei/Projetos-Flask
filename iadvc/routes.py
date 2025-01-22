from main import app


@app.route('/')
def home():
    return 'Ola Mundo, meu primeiro CRUD'