#-*-coding:utf-8-*-
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from gaesessions import get_current_session
import app


def get_current_user():
    session = get_current_session()
    if session.has_key('user_id'):
        return User.get_by_id(session['user_id'])
    return None


class BindUserHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('bind user')

    def post(self):
        self.response.out.write('bind user')


class GoogleLoginHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<a href="'+GoogleAccountType().get_login_url()+'">login</a>')


class LoginBackHandler(webapp.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        type_code_value = GoogleAccountType.get_code()
        open_id_value = google_user.federated_identity()
        account_key_name = Account.create_key_name(type_code=type_code_value, open_id=open_id_value)
        account = Account.get_by_key_name(account_key_name)
        if account == None:
            account = Account(key_name=account_key_name, type_code=type_code_value, open_id=open_id_value,\
                                email=google_user.email(), nickname=google_user.nickname())
            account.put()
        if account.canBindUser():
            add_account_to_bind_list(account)
            self.redirect(app.get_config().get('user/bind_user_url'))
        set_current_user(account.user)


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

    @staticmethod
    def get_code():
        return None


class Account(db.Model):
    type_code = db.StringProperty(required=True)
    open_id = db.IntegerProperty(required=True)
    user = db.ReferenceProperty(User, indexed=True)
    email = db.EmailProperty()
    nickname = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)

    @staticmethod
    def load_by_open_id(open_id, type_code):
        return Account.all().filter('open_id =', open_id)\
                .filter('type_code =', type_code).get()

    @staticmethod
    def create_key_name(open_id, type_code):
        return '_'.join([type_code, open_id])


class GoogleAccountType(AccountType):
    def __init__(self):
        self.login_url = users.create_login_url('/loginback?type=google')

    @staticmethod
    def get_code():
        return u'google'


CONFIGS = {
    'modules': {'user':{'version':'0.1'}},
    'routers':[
        ('/google_login', GoogleLoginHandler),
        ('/loginback', LoginBackHandler),
        ('/bind_user', BindUserHandler)
        ],
    'user':{
        # 用户帐户类型
        'account_types':{GoogleAccountType.get_code():GoogleAccountType()},
        'bind_user_url':'/bind_user'
        }
    }
