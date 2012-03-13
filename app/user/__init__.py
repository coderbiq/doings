#-*-coding:utf-8-*-
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
import app

class GoogleLoginHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<a href="'+GoogleAccountType().get_login_url()+'">login</a>')


class LoginBackHandler(webapp.RequestHandler):
    def get(self):
        html = ''
        user = users.get_current_user()
        html = html + "user nickname %s" % user.nickname()
        html = html + "login type %s" % self.request.get('type')
        self.response.out.write(html)


def get_login_urls():
    account_types = app.get_config().get('user/account_types')
    login_urls = []
    for account_type in account_types.values():
        login_urls.append(account_type.get_login_url())
    return login_urls


class User(db.Model):
    nickname = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)


class AccountType(object):
    def get_login_url(self):
        return self.login_url


class Account(db.Model):
    type_code = db.StringProperty(required=True)
    user = db.ReferenceProperty(User, indexed=True)
    open_id = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)


class GoogleAccountType(AccountType):
    def __init__(self):
        self.login_url = users.create_login_url('/loginback?type=google')


CONFIGS = {
    'modules': {'user':{'version':'0.1'}},
    'routers':[
        ('/google_login', GoogleLoginHandler),
        ('/loginback', LoginBackHandler)
        ],
    'user':{
        # 用户帐户类型
        'account_types':{'google':GoogleAccountType()}
        }
    }
