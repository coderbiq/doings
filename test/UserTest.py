#-*-coding:utf-8-*-

import unittest
import app.user

class UserTest(unittest.TestCase):

    def test_get_login_urls(self):
        login_urls = app.user.get_login_urls()
        self.assertEqual(type(login_urls), list)
        self.assertTrue(len(login_urls) > 0)

    def test_create_account(self):
        count = app.user.Account.all().count()
        account = app.user.Account(type_code='google', open_id=1)
        account.put()
        self.assertEqual(app.user.Account.all().count(), count+1)

    def test_load_account_by_open_id(self):
        type_code_value = app.user.GoogleAccountType.get_code()
        account_object = app.user.Account(type_code=type_code_value, 
                                            open_id=1)
        account_object.put()
        account = app.user.Account.load_by_open_id(1, type_code_value)
        self.assertEqual(account.type_code, type_code_value)
        self.assertEqual(account.open_id, 1)
