#-*-coding:utf-8-*-
from google.appengine.ext import db
import app


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
        self.login_url = 'abc'


CONFIGS = {
    'modules': {'user':{'version':'0.1'}},
    'routers':[],
    'user':{
        # 用户帐户类型
        'account_types':{'google':GoogleAccountType()}
        }
    }
