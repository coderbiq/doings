#-*-coding:utf-8-*-
from google.appengine.ext import webapp


class TestHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('test 2 handler get')


CONFIGS = {
    't2': {
        'abc': 'rrr'
        },
    'modules': {
            't2':{'version': '0.2'}
        },
    'routers': [
        ('/tmodule2', TestHandler)
        ]
    }
