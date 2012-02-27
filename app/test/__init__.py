#-*-coding:utf-8-*-
from google.appengine.ext import webapp


class TestHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('test handler get')

CONFIGS = {
    'modules': {
        'test': {
            'version': '0.1'
            }
        },
    'routers':[
        ('/tmodule', TestHandler)
        ]
    }
