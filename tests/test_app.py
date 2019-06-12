"""Tests and documents use of the Web UI

Any client must make this type of request to Web UI
Made from Flask testing docs
http://flask.pocoo.org/docs/1.0/testing/

"""
import unittest

from app.views import app


# mysession = MySession(Base, test=True)
# dbsession = mysession.session
# engine = mysession.engine
# app = configure_app()
# Base.metadata.create_all(engine)



class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        self.logout()

    def get_token(self, url):
        response = self.app.get(url, follow_redirects=True)
        csrf_token = response.data.decode()
        begin = csrf_token.find('csrf_token"') + 10
        end = csrf_token.find('username"') - 10
        csrf_token = csrf_token[begin: end]
        begin = csrf_token.find('value="') + 7
        end = csrf_token.find('/>')
        self.csrf_token = csrf_token[begin: end]
        return self.csrf_token

    def login(self, username, senha):
        self.get_token('/login')
        return self.app.post('/login', data=dict(
            username=username,
            senha=senha,
            csrf_token=self.csrf_token
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_home(self):
        rv = self.app.get('/')
        assert b'OK' in rv.data

    def test_param(self):
        rv = self.app.get('/param/fit-partners')
        assert b'fit-partners' in rv.data
