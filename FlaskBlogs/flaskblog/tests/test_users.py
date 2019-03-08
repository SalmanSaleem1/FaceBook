import unittest
from flask_testing import TestCase
from flaskblog.Models import User

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # login
        response = self.client.post('/login', **self.credentials)
        # should be logged in now, fails however
        self.assertTrue(response.context['user'].is_active)


if __name__ == '__main__':
    unittest.main()
