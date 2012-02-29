#-*-coding:utf-8-*-

import unittest
import app


CONFIG_1 = {
    'modules':{
        'test1':{'version':'0.1'}
    },
    'routers':[('r1', 'r1')],
    'test1':{
        'abc':{'ert':'123'},
        'ert':'222'
    }
}

CONFIG_2 = {
    'modules':{
        'test2':{'version':'0.2'}
    },
    'routers':[('r2', 'r2')],
    'test1':{
        'abc':{'ert':'321'}
    }
}

CONFIG = {
    'modules':{
        'test1':{'version':'0.1'},
        'test2':{'version':'0.2'}
    },
    'routers':[('r1', 'r1'),('r2', 'r2')],
    'test1':{
        'abc':{'ert':'321'},
        'ert':'222'
    }
}

class ConfigTest(unittest.TestCase):

    def test_get(self):
        config = app.get_config()
        self.assertEqual(config.get('modules/test/version'), '0.1')
        self.assertEqual(config.get('modules/t2/version'), '0.2')
        self.assertEqual(config.get('t2/abc'), 'rrr')

    def test_get_routers(self):
        routers = app.get_config().get('routers');
        self.assertTrue(len(routers) > 1)

    def test_extends_config(self):
        config = app.get_config()
        config.extends(CONFIG_1)
        config.extends(CONFIG_2)
        self.assertEqual(config.configs, CONFIG)
