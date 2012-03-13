#-*-coding:utf-8-*-

import unittest
import app.user

class UserTest(unittest.TestCase):

    def test_get_login_urls(self):
        login_urls = app.user.get_login_urls()
        self.assertEqual(type(login_urls), list)
        self.assertTrue(len(login_urls) > 0)
