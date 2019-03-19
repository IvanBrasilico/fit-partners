from flask import Flask

from app.main import configure_app
from app.models import configure_db

app = configure_app()
configure_db(app)

@app.route('/')
def hello():
    return 'OK, mundo!'


@app.route('/param/<param>')
def hello_param(param):
    return f'Recebeu {param}!'

if __name__ == '__main__':
    app.run()