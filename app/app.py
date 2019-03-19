from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'OK, mundo!'


@app.route('/<param>')
def hello_param(param):
    return f'Recebeu {param}!'

if __name__ == '__main__':
    app.run()