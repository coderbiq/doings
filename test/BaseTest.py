#-*-coding:utf-8-*-

import unittest,os
from google.appengine.ext import db,testbed,webapp


def setCurrentUser(email, user_id, is_admin=False):
    os.environ['USER_EMAIL'] = email or ''
    os.environ['USER_ID'] = user_id or ''
    os.environ['USER_IS_ADMIN'] = '1' if is_admin else '0'

def logoutCurrentUser():
    setCurrentUser(None, None)


class BaseTest(unittest.TestCase):
    def setup(self):
        self.testbed = tested.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()


#class TestProject(unittest.TestCase):
#
#    def setUp(self):
#        self.testbed = testbed.Testbed()
#        self.testbed.activate()
#        self.testbed.init_user_stub()
#
##    def tearDown(self):
##        self.testbed.deactivate()
#
#    def test2(self):
#        setCurrentUser('abc','1')
#        user = users.get_current_user()
#        self.assertEqual(user, users.User('abc',_user_id=1))
#
#    def test_request(self):
#        request = webapp.Request.blank('/init')
#        request.method = 'GET'
#        # get请求参数
#        request.query_string = 'name=Joe&email=joe@example.com'
#        # post 请求参数
#        request.body = 'name=Joe&email=joe@example.com'
#        response = webapp.Response()
#        handler = ctrac.TestHandler()
#        handler.initialize(request, response)
#        handler.get()
##        handler.post()
#        self.assertEqual(response.out.getvalue(), u'Joe')
