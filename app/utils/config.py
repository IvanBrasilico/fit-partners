import pickle
import os
basedir = os.path.abspath(os.path.dirname(__file__))


def get_secret():
    secret_file = os.path.join(basedir, 'SECRET')
    try:
        with open(secret_file, 'rb') as secret:
            try:
                SECRET = pickle.load(secret)
            except pickle.PickleError:
                SECRET = None
    except FileNotFoundError:
        SECRET = None

    if SECRET is None:
        SECRET = os.urandom(24)
        with open(secret_file, 'wb') as out:
            pickle.dump(SECRET, out, pickle.HIGHEST_PROTOCOL)
    return SECRET


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = get_secret()
    SQLALCHEMY_DATABASE_URI = os.environ.get('FIT_DB_URL')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True