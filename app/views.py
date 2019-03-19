from flask import Flask


app = Flask(__name__)

def configure_app():
    return app

@app.route('/')
def hello():
    return 'OK, mundo!'


@app.route('/param/<param>')
def hello_param(param):
    return f'Recebeu {param}!'

if __name__ == '__main__':
    app.run()